"""
AI Compliance Sherpa - Interactive Streamlit Dashboard
Displays EU AI Act classification results with custom system analysis
"""

import streamlit as st
import json
import pandas as pd
from datetime import datetime
from src.sherpa.agent import SherpaAgent
from src.schemas import Questionnaire, ClassificationResult
from src.classification import classify_system
from src.compliance_report import ComplianceReportGenerator, ComplianceStatus


# Page configuration
st.set_page_config(
    page_title="AI Compliance Sherpa",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main-title {
        color: #1f77b4;
        padding: 20px 0;
        border-bottom: 3px solid #1f77b4;
    }
    .high-risk {
        background-color: #ffebee;
        color: #c62828;
        padding: 10px;
        border-radius: 5px;
        font-weight: bold;
    }
    .limited-risk {
        background-color: #fff3e0;
        color: #e65100;
        padding: 10px;
        border-radius: 5px;
        font-weight: bold;
    }
    .minimal-risk {
        background-color: #e8f5e9;
        color: #2e7d32;
        padding: 10px;
        border-radius: 5px;
        font-weight: bold;
    }
    .prohibited {
        background-color: #fce4ec;
        color: #880e4f;
        padding: 10px;
        border-radius: 5px;
        font-weight: bold;
    }
    .info-box {
        background-color: #f0f7ff;
        border-left: 4px solid #1f77b4;
        padding: 15px;
        margin: 10px 0;
        border-radius: 3px;
    }
    </style>
""", unsafe_allow_html=True)

# Load test systems
@st.cache_data
def load_test_systems():
    """Load test systems from JSON file"""
    with open('test_systems.json', 'r') as f:
        return json.load(f)

# Initialize session state
if 'analysis_results' not in st.session_state:
    st.session_state.analysis_results = []
if 'selected_systems' not in st.session_state:
    st.session_state.selected_systems = []
if 'custom_result' not in st.session_state:
    st.session_state.custom_result = None

# Title
st.markdown('<h1 class="main-title">⚖️ AI Compliance Sherpa</h1>', unsafe_allow_html=True)
st.markdown("**Assess your AI systems for EU AI Act compliance**")

# Create tabs
tab1, tab2 = st.tabs(["📋 Pre-Built Test Systems", "🔧 Custom AI System Analysis"])

# ==================== TAB 1: TEST SYSTEMS ====================
with tab1:
    st.markdown("### Analyze Pre-Built Test Systems")
    st.markdown('<div class="info-box">Select one or more test systems from the sidebar to analyze their EU AI Act compliance status.</div>', unsafe_allow_html=True)
    
    # Load test systems
    test_systems = load_test_systems()
    system_names = [sys['name'] for sys in test_systems]
    
    # Sidebar for system selection
    st.sidebar.markdown("---")
    st.sidebar.header("📋 Test Systems")
    
    # Multi-select for systems
    selected_names = st.sidebar.multiselect(
        "Select Systems to Analyze",
        options=system_names,
        default=[],
        help="Choose one or more systems to analyze."
    )
    
    # Store selected indices
    selected_indices = [i for i, sys in enumerate(test_systems) if sys['name'] in selected_names]
    
    # Settings in sidebar
    st.sidebar.markdown("---")
    st.sidebar.subheader("⚙️ Display Settings")
    show_details = st.sidebar.checkbox("Show Detailed Reports", value=False)
    show_articles = st.sidebar.checkbox("Show Applicable Articles", value=True)
    
    # Display selected count
    if selected_names:
        st.info(f"✓ {len(selected_names)} system(s) selected")
    else:
        st.warning("No systems selected. Choose systems from the sidebar to begin analysis.")
    
    # Analyze button
    col1, col2, col3 = st.columns([1, 1, 2])
    with col1:
        analyze_button = st.button("🔍 Analyze", type="primary", key="analyze_test_systems")
    
    if analyze_button:
        if not selected_names:
            st.error("Please select at least one system to analyze.")
        else:
            # Initialize agent
            with st.spinner("Initializing compliance agent..."):
                try:
                    agent = SherpaAgent()
                except Exception as e:
                    st.error(f"Failed to initialize agent: {e}")
                    st.stop()
            
            # Progress tracking
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            # Analyze each selected system
            results = []
            for idx, system_index in enumerate(selected_indices):
                system = test_systems[system_index]
                progress = (idx + 1) / len(selected_indices)
                
                status_text.text(f"Analyzing: {system['name']}...")
                progress_bar.progress(progress)
                
                try:
                    # Handle nested format
                    if 'basic_info' in system:
                        basic_info = system['basic_info']
                        data_types = basic_info['data_types']
                        autonomous = basic_info['autonomous']
                        affects_rights = basic_info['affects_rights']
                        use_case = basic_info['use_case']
                    else:
                        data_types = system.get('data_types', 'N/A')
                        autonomous = system.get('autonomous', False)
                        affects_rights = system.get('affects_rights', False)
                        use_case = system.get('use_case', 'N/A')
                    
                    # Create questionnaire
                    questionnaire = Questionnaire(
                        name=system['name'],
                        purpose=system['purpose'],
                        data_types=data_types,
                        autonomous=autonomous,
                        affects_rights=affects_rights,
                        use_case=use_case
                    )
                    
                    # Build description
                    description = f"""
Classify this AI system under the EU AI Act:

System: {system['name']}
Purpose: {system['purpose']}
Data: {data_types}
Autonomous: {autonomous}
Affects Rights: {affects_rights}
Use Case: {use_case}

Provide classification and explanation.
"""
                    
                    # Get classification from agent
                    agent_response = agent.classify(description)
                    result = classify_system(questionnaire, agent_response)
                    results.append((result, system))
                    
                except Exception as e:
                    st.warning(f"Error analyzing {system['name']}: {str(e)}")
                    continue
            
            status_text.text("Analysis complete!")
            progress_bar.progress(1.0)
            
            # Store results
            st.session_state.analysis_results = results
            st.success(f"✓ Successfully analyzed {len(results)} system(s)")
    
    # Display results
    if st.session_state.analysis_results:
        st.markdown("---")
        st.markdown("## 📊 Assessment Results")
        
        # Results table
        results_data = []
        for result, system in st.session_state.analysis_results:
            expected = system.get('expected_classification', 'UNKNOWN')
            match = "✅" if result.risk_classification == expected else "⚠️"
            
            results_data.append({
                "System": result.system_name,
                "Classification": result.risk_classification,
                "Confidence": f"{int(result.confidence_score * 100)}%",
                "Expected": expected,
                "Match": match
            })
        
        results_df = pd.DataFrame(results_data)
        st.dataframe(results_df, use_container_width=True, hide_index=True)
        
        # Summary metrics
        col1, col2, col3, col4 = st.columns(4)
        
        classifications = [r[0].risk_classification for r in st.session_state.analysis_results]
        
        with col1:
            prohibited = classifications.count("PROHIBITED")
            st.metric("🚫 Prohibited", prohibited)
        
        with col2:
            high_risk = classifications.count("HIGH_RISK")
            st.metric("⚠️ High Risk", high_risk)
        
        with col3:
            limited = classifications.count("LIMITED_RISK")
            st.metric("ℹ️ Limited Risk", limited)
        
        with col4:
            minimal = classifications.count("MINIMAL_RISK")
            st.metric("✅ Minimal Risk", minimal)
        
        # Detailed reports
        if show_details:
            st.markdown("---")
            st.markdown("## 📄 Detailed Compliance Assessment")
            
            for idx, (result, system) in enumerate(st.session_state.analysis_results, 1):
                with st.expander(f"{idx}. {result.system_name}", expanded=(idx == 1)):
                    # Risk classification
                    col1, col2 = st.columns([2, 1])
                    
                    with col1:
                        risk_class = result.risk_classification
                        confidence = int(result.confidence_score * 100)
                        
                        if risk_class == "PROHIBITED":
                            st.markdown(f'<div class="prohibited">🚫 PROHIBITED - {confidence}% confidence</div>', unsafe_allow_html=True)
                        elif risk_class == "HIGH_RISK":
                            st.markdown(f'<div class="high-risk">⚠️ HIGH RISK - {confidence}% confidence</div>', unsafe_allow_html=True)
                        elif risk_class == "LIMITED_RISK":
                            st.markdown(f'<div class="limited-risk">ℹ️ LIMITED RISK - {confidence}% confidence</div>', unsafe_allow_html=True)
                        else:
                            st.markdown(f'<div class="minimal-risk">✅ MINIMAL RISK - {confidence}% confidence</div>', unsafe_allow_html=True)
                    
                    with col2:
                        expected = system.get('expected_classification', 'UNKNOWN')
                        st.metric("Expected", expected)
                    
                    # Compliance criteria table
                    st.markdown("### EU AI Act Compliance Criteria")
                    
                    # Build questionnaire data (Employment, Finance, Infrastructure focus)
                    questionnaire_data = {
                        'q5_recruitment_selection': system.get('eu_ai_act_questions', {}).get('q5_recruitment_selection'),
                        'q6_employment_conditions': system.get('eu_ai_act_questions', {}).get('q6_employment_conditions'),
                        'q7_biometric_identification': system.get('eu_ai_act_questions', {}).get('q7_biometric_identification'),
                        'q8_categorization_sensitive': system.get('eu_ai_act_questions', {}).get('q8_categorization_sensitive'),
                        'q9_critical_infrastructure': system.get('eu_ai_act_questions', {}).get('q9_critical_infrastructure'),
                        'q10_credit_scoring': system.get('eu_ai_act_questions', {}).get('q10_credit_scoring'),
                    }
                    
                    # Generate criteria
                    generator = ComplianceReportGenerator()
                    criteria = generator.generate_criteria_table(questionnaire_data)
                    applicable_criteria = [c for c in criteria if c.applicable]
                    
                    # Display criteria table
                    criteria_data = []
                    for criterion in applicable_criteria:
                        if criterion.status == ComplianceStatus.PROHIBITED:
                            status_symbol = "🚫"
                            status_text = "PROHIBITED"
                        elif criterion.status == ComplianceStatus.HIGH_RISK:
                            status_symbol = "❌"
                            status_text = "HIGH RISK"
                        elif criterion.status == ComplianceStatus.LIMITED_RISK:
                            status_symbol = "⚠️"
                            status_text = "LIMITED RISK"
                        elif criterion.status == ComplianceStatus.COMPLIANT:
                            status_symbol = "✅"
                            status_text = "COMPLIANT"
                        else:
                            status_symbol = "⊘"
                            status_text = "N/A"
                        
                        criteria_data.append({
                            "Category": criterion.category,
                            "Criterion": criterion.criterion,
                            "Status": f"{status_symbol} {status_text}",
                            "Explanation": criterion.explanation
                        })
                    
                    if criteria_data:
                        criteria_df = pd.DataFrame(criteria_data)
                        st.dataframe(criteria_df, use_container_width=True, hide_index=True)
                    
                    # Articles
                    if show_articles and result.applicable_articles:
                        st.markdown("**📋 Applicable Articles:**")
                        articles = ", ".join([f"Article {a.article_number}" for a in result.applicable_articles])
                        st.info(articles)
                    
                    # Obligations
                    if result.compliance_obligations:
                        st.markdown("**✓ Compliance Obligations:**")
                        for obligation in result.compliance_obligations:
                            st.write(f"• {obligation}")
                    
                    # Recommendations
                    if result.recommendations:
                        st.markdown("**💡 Recommendations:**")
                        for recommendation in result.recommendations:
                            st.write(f"• {recommendation}")

# ==================== TAB 2: CUSTOM ANALYSIS ====================
with tab2:
    st.markdown("### Analyze Your Custom AI System")
    st.markdown('<div class="info-box">Describe your AI system in detail below. The compliance agent will analyze it and provide an EU AI Act compliance assessment.</div>', unsafe_allow_html=True)
    
    # Custom system input form
    col1, col2 = st.columns(2)
    
    with col1:
        custom_name = st.text_input(
            "AI System Name",
            placeholder="e.g., Employee Resume Screening Tool",
            help="Give your AI system a clear, descriptive name"
        )
    
    with col2:
        custom_sector = st.selectbox(
            "Industry Sector",
            ["Finance/Banking", "Employment/HR", "Healthcare", "Public Services", 
             "Law Enforcement", "Infrastructure", "E-commerce", "Social Media", "Other"],
            help="Select the primary industry sector"
        )
    
    custom_purpose = st.text_area(
        "System Purpose & Use Case",
        placeholder="Describe what this AI system does and in what context it operates...",
        height=100,
        help="Provide a clear description of the system's purpose and how it's used"
    )
    
    custom_data = st.text_area(
        "Data Types Processed",
        placeholder="List the types of data your system processes (e.g., personal information, financial data, biometric data, educational records)...",
        height=80,
        help="Describe all categories of data the system processes"
    )
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        custom_autonomous = st.selectbox(
            "Autonomous Decision Making",
            ["Yes", "No", "Partially (some decisions only)"],
            help="Does the system make decisions without human intervention?"
        )
    
    with col2:
        custom_affects_rights = st.selectbox(
            "Affects Fundamental Rights",
            ["Yes", "No", "Potentially"],
            help="Do the system's decisions or operations affect fundamental rights?"
        )
    
    with col3:
        custom_human_oversight = st.selectbox(
            "Human Oversight",
            ["No oversight", "Minimal", "Moderate", "Strong", "Full"],
            help="What level of human oversight does the system have?"
        )
    
    # Advanced questions
    with st.expander("Advanced Compliance Questions", expanded=False):
        st.markdown("Answer these detailed questions to enable comprehensive compliance assessment:")
        
        custom_q5 = st.selectbox(
            "Q5: Does your system make recruitment or selection decisions?",
            ["No", "Yes - filters candidates", "Yes - makes final decisions", "Yes - but with strong human oversight"],
            key="custom_q5"
        )
        
        custom_q6 = st.selectbox(
            "Q6: Does your system evaluate employment conditions or performance?",
            ["No", "Yes - performance evaluation", "Yes - determines employment terms", "Yes - with human oversight"],
            key="custom_q6"
        )
        
        custom_q7 = st.selectbox(
            "Q7: Does your system use biometric identification?",
            ["No", "Yes - physical verification at location", "Yes - uses biometric data", "Yes - real-time remote biometric ID"],
            key="custom_q7"
        )
        
        custom_q8 = st.selectbox(
            "Q8: Does your system categorize individuals based on sensitive attributes?",
            ["No", "Yes - race/ethnicity/national origin", "Yes - gender/sexual orientation", "Yes - religion/disability", "Yes - multiple sensitive attributes"],
            key="custom_q8"
        )
        
        custom_q9 = st.selectbox(
            "Q9: Is this system a critical infrastructure component?",
            ["No", "Yes - important but not critical", "Yes - critical infrastructure"],
            key="custom_q9"
        )
        
        custom_q10 = st.selectbox(
            "Q10: Does your system assess credit or financial risk?",
            ["No", "Yes - financial risk scoring", "Yes - credit decisions", "Yes - but human decides"],
            key="custom_q10"
        )
    
    custom_notes = st.text_area(
        "Additional Notes (Optional)",
        placeholder="Any other relevant information (e.g., 'System is still in testing', 'We have completed a DPIA', etc.)...",
        height=60
    )
    
    # Analyze button
    col1, col2, col3 = st.columns([1, 3, 1])
    with col1:
        custom_analyze = st.button("🔍 Analyze Custom System", type="primary", key="analyze_custom", use_container_width=True)
    
    if custom_analyze:
        if not custom_name or not custom_purpose or not custom_data:
            st.error("Please fill in at least the System Name, Purpose, and Data Types fields.")
        else:
            with st.spinner("Analyzing your AI system..."):
                try:
                    agent = SherpaAgent()
                except Exception as e:
                    st.error(f"Failed to initialize agent: {e}")
                    st.stop()
                
                # Build full system description
                full_description = f"""
Analyze and classify this AI system under the EU AI Act:

**System Name:** {custom_name}
**Industry Sector:** {custom_sector}

**Purpose & Use Case:**
{custom_purpose}

**Data Types Processed:**
{custom_data}

**Technical Characteristics:**
- Autonomous Decision Making: {custom_autonomous}
- Affects Fundamental Rights: {custom_affects_rights}
- Human Oversight: {custom_human_oversight}

**Specific Applications:**
- Recruitment/Selection Decisions: {custom_q5}
- Employment Evaluation: {custom_q6}
- Biometric Identification: {custom_q7}
- Sensitive Attribute Categorization: {custom_q8}
- Critical Infrastructure: {custom_q9}
- Credit/Financial Assessment: {custom_q10}

{f"**Additional Context:** {custom_notes}" if custom_notes else ""}

Provide a detailed EU AI Act compliance classification, applicable articles, compliance obligations, and recommendations.
"""
                
                try:
                    # Create questionnaire
                    questionnaire = Questionnaire(
                        name=custom_name,
                        purpose=custom_purpose,
                        data_types=custom_data,
                        autonomous=(custom_autonomous == "Yes"),
                        affects_rights=(custom_affects_rights == "Yes"),
                        use_case=custom_sector,
                        additional_notes=custom_notes
                    )
                    
                    # Get classification
                    agent_response = agent.classify(full_description)
                    result = classify_system(questionnaire, agent_response)
                    st.session_state.custom_result = (result, {
                        'name': custom_name,
                        'purpose': custom_purpose,
                        'eu_ai_act_questions': {
                            'q5_recruitment_selection': 'yes' if 'Yes' in custom_q5 else False,
                            'q6_employment_conditions': 'yes' if 'Yes' in custom_q6 else False,
                            'q7_biometric_identification': 'yes' if 'Yes' in custom_q7 else False,
                            'q8_categorization_sensitive': 'yes' if 'Yes' in custom_q8 else False,
                            'q9_critical_infrastructure': 'yes' if 'Yes' in custom_q9 else False,
                            'q10_credit_scoring': 'yes' if 'Yes' in custom_q10 else False,
                        }
                    })
                    
                    st.success("✓ Analysis complete!")
                    
                except Exception as e:
                    st.error(f"Error analyzing system: {str(e)}")
    
    # Display custom results
    if st.session_state.custom_result:
        result, system_info = st.session_state.custom_result
        
        st.markdown("---")
        st.markdown("## 📊 Compliance Assessment Results")
        
        # Classification display
        col1, col2 = st.columns([2, 1])
        
        with col1:
            risk_class = result.risk_classification
            confidence = int(result.confidence_score * 100)
            
            if risk_class == "PROHIBITED":
                st.markdown(f'<div class="prohibited">🚫 PROHIBITED - {confidence}% confidence</div>', unsafe_allow_html=True)
            elif risk_class == "HIGH_RISK":
                st.markdown(f'<div class="high-risk">⚠️ HIGH RISK - {confidence}% confidence</div>', unsafe_allow_html=True)
            elif risk_class == "LIMITED_RISK":
                st.markdown(f'<div class="limited-risk">ℹ️ LIMITED RISK - {confidence}% confidence</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="minimal-risk">✅ MINIMAL RISK - {confidence}% confidence</div>', unsafe_allow_html=True)
        
        # Compliance criteria table
        st.markdown("### EU AI Act Compliance Criteria")
        
        generator = ComplianceReportGenerator()
        criteria = generator.generate_criteria_table(system_info['eu_ai_act_questions'])
        applicable_criteria = [c for c in criteria if c.applicable]
        
        criteria_data = []
        for criterion in applicable_criteria:
            if criterion.status == ComplianceStatus.PROHIBITED:
                status_symbol = "🚫"
                status_text = "PROHIBITED"
            elif criterion.status == ComplianceStatus.HIGH_RISK:
                status_symbol = "❌"
                status_text = "HIGH RISK"
            elif criterion.status == ComplianceStatus.LIMITED_RISK:
                status_symbol = "⚠️"
                status_text = "LIMITED RISK"
            elif criterion.status == ComplianceStatus.COMPLIANT:
                status_symbol = "✅"
                status_text = "COMPLIANT"
            else:
                status_symbol = "⊘"
                status_text = "N/A"
            
            criteria_data.append({
                "Category": criterion.category,
                "Criterion": criterion.criterion,
                "Status": f"{status_symbol} {status_text}",
                "Explanation": criterion.explanation
            })
        
        if criteria_data:
            criteria_df = pd.DataFrame(criteria_data)
            st.dataframe(criteria_df, use_container_width=True, hide_index=True)
        
        # Articles
        if result.applicable_articles:
            st.markdown("**📋 Applicable EU AI Act Articles:**")
            articles = ", ".join([f"Article {a.article_number}" for a in result.applicable_articles])
            st.info(articles)
        
        # Obligations
        if result.compliance_obligations:
            st.markdown("**✓ Compliance Obligations:**")
            for obligation in result.compliance_obligations:
                st.write(f"• {obligation}")
        
        # Recommendations
        if result.recommendations:
            st.markdown("**💡 Recommendations:**")
            for recommendation in result.recommendations:
                st.write(f"• {recommendation}")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; font-size: 0.9em;">
    <p><strong>AI Compliance Sherpa</strong> - EU AI Act Assessment Tool</p>
    <p>For demo purposes. Always consult with your legal and compliance team for final determinations.</p>
</div>
""", unsafe_allow_html=True)
