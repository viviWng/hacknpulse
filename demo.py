"""Demo script - End-to-end classification of test systems"""
import json
import asyncio
import sys
from pathlib import Path

# Add project to path
sys.path.insert(0, str(Path(__file__).parent))

from src.schemas import Questionnaire
from src.sherpa.agent import SherpaAgent
from src.classification import classify_system
from src.output import format_summary, format_markdown_report


async def demo():
    """Run demo classification of test AI systems"""
    
    print("\n" + "="*80)
    print("🎯 AI COMPLIANCE SHERPA - DEMO")
    print("="*80 + "\n")
    
    # Load test systems
    with open("test_systems.json", "r") as f:
        test_systems = json.load(f)
    
    # Initialize agent
    print("🤖 Initializing Sherpa Agent...")
    try:
        agent = SherpaAgent()
        print("✅ Agent initialized\n")
    except Exception as e:
        print(f"❌ Failed to initialize agent: {e}")
        print("Make sure AZURE_OPENAI_API_KEY and AZURE_OPENAI_ENDPOINT are set in .env")
        return
    
    # Classify each test system
    results = []
    for i, system in enumerate(test_systems, 1):  # Demo with all systems
        print(f"\n{'─'*80}")
        print(f"📋 System {i}: {system['name']}")
        print(f"{'─'*80}")
        
        try:
            # Handle both new detailed format and old simple format
            if 'basic_info' in system:
                # New detailed format
                basic_info = system['basic_info']
                data_types = basic_info['data_types']
                autonomous = basic_info['autonomous']
                affects_rights = basic_info['affects_rights']
                use_case = basic_info['use_case']
            else:
                # Old simple format (backward compatible)
                data_types = system['data_types']
                autonomous = system['autonomous']
                affects_rights = system['affects_rights']
                use_case = system['use_case']
            
            # Create questionnaire
            questionnaire = Questionnaire(
                name=system['name'],
                purpose=system['purpose'],
                data_types=data_types,
                autonomous=autonomous,
                affects_rights=affects_rights,
                use_case=use_case
            )
            
            # Build description for agent with more context if available
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
            print("🔍 Analyzing system...")
            agent_response = agent.classify(description)
            
            # Build result
            result = classify_system(questionnaire, agent_response)
            results.append(result)
            
            # Display summary
            print(format_summary(result))
            print(f"Expected: {system['expected_classification']}")
            print(f"Articles: {[a.article_number for a in result.applicable_articles]}")
            
        except Exception as e:
            print(f"❌ Error classifying {system['name']}: {e}")
            continue
    
    # Summary
    print(f"\n{'='*80}")
    print(f"📊 DEMO SUMMARY")
    print(f"{'='*80}\n")
    
    for result in results:
        print(format_summary(result))
    
    # Generate full report for first system
    if results:
        print(f"\n{'─'*80}")
        print("📄 SAMPLE REPORT (First System)")
        print(f"{'─'*80}\n")
        print(format_markdown_report(results[0]))
    
    print(f"\n{'='*80}")
    print("✅ Demo Complete")
    print(f"{'='*80}\n")


if __name__ == "__main__":
    asyncio.run(demo())
