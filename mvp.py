from flask import Flask, request, jsonify
import openai
from fpdf import FPDF
import os

app = Flask(__name__)

openai.api_key = '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'

def categorize_risk(ai_solution_description):
    prompt = f"Categorize the following AI solution according to the EU AI Act (Unacceptable, Limited, High risk):\n\n{ai_solution_description}"
    response = openai.ChatCompletion.create(
       model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an AI compliance agent that categorizes AI solutions according to the EU AI Act."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message['content'].strip()

# méthode pour créer le documentation technique (les étapes à suivre pour rendre le solution AI conforme à la loi)
def generate_compliance_steps(ai_solution_description):
    prompt = f"Provide step-by-step guidance to make the following high-risk AI solution compliant with the EU AI Act:\n\n{ai_solution_description}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an AI compliance agent that provides guidance to make AI solutions compliant with the EU AI Act."},
            {"role": "user", "content": prompt}
        ]
    )
    # return response.choices[0].message['content'].strip()
    compliance_steps_content = response.choices[0].message['content'].strip()

    # Create a PDF file
    pdf = FPDF()
    pdf.add_page()
    # Add a Unicode-compatible font
    pdf.add_font('DejaVu', '', 'DejaVuSans.ttf', uni=True)
    pdf.set_font('DejaVu', '', 12)
    
    pdf.multi_cell(0, 10, compliance_steps_content)

    # Ensure the 'web' directory exists
    if not os.path.exists('doc_technique'):
        os.makedirs('doc_technique')

    # Save the PDF to the 'web' directory
    pdf_output_path = os.path.join('doc_technique', 'doc_tech.pdf')
    pdf.output(pdf_output_path)

    return pdf_output_path

def create_user_manual(ai_solution_description):
    prompt = f"Create a user manual for the following AI solution in compliance with the EU AI Act. Ask the user pertinent questions to gather the necessary information:\n\n{ai_solution_description}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an AI compliance agent that creates user manuals for AI solutions in compliance with the EU AI Act."},
            {"role": "user", "content": prompt}
        ]
    )
    # return response.choices[0].message['content'].strip()
    user_manual_content = response.choices[0].message['content'].strip()

    # Create a PDF file
    pdf = FPDF()
    pdf.add_page()
    # Add a Unicode-compatible font
    pdf.add_font('DejaVu', '', 'DejaVuSans.ttf', uni=True)
    pdf.set_font('DejaVu', '', 12)
    
    pdf.multi_cell(0, 10, user_manual_content)

    # Ensure the 'web' directory exists
    if not os.path.exists('web'):
        os.makedirs('web')

    # Save the PDF to the 'web' directory
    pdf_output_path = os.path.join('web', 'user_manual.pdf')
    pdf.output(pdf_output_path)

    return pdf_output_path

def main():
    # Step 1: AI solution description (user provides it)
    ai_solution_description = input("Describe your AI solution in detail (e.g., purpose, data used, decision-making process): ")

    # Step 2: Categorize the AI solution risk
    risk_category = categorize_risk(ai_solution_description)
    print(f"\nRisk Category: {risk_category}")

    # Step 3: If the solution is high risk, provide compliance steps
    if any(keyword in risk_category.lower() for keyword in ["high risk", "high-risk", "limited"]):
        compliance_steps_path = generate_compliance_steps(ai_solution_description)
        print(f"\nTechnical doc saved at: {compliance_steps_path}")
        # print("\nCompliance Steps:\n", compliance_steps)

        # Step 4: Create a user manual
        user_manual_path = create_user_manual(ai_solution_description)
        print(f"\nUser Manual saved at: {user_manual_path}")
    else:
        print("No further action needed for this risk category.")

@app.route('/categorize_risk', methods=['POST'])
def api_categorize_risk():
    data = request.json
    ai_solution_description = data.get('ai_solution_description')
    risk_category = categorize_risk(ai_solution_description)
    return jsonify({"risk_category": risk_category})

@app.route('/generate_compliance_steps', methods=['POST'])
def api_generate_compliance_steps():
    data = request.json
    ai_solution_description = data.get('ai_solution_description')
    compliance_steps = generate_compliance_steps(ai_solution_description)
    return jsonify({"compliance_steps": compliance_steps})

@app.route('/create_user_manual', methods=['POST'])
def api_create_user_manual():
    data = request.json
    ai_solution_description = data.get('ai_solution_description')
    user_manual_path = create_user_manual(ai_solution_description)
    return jsonify({"user_manual_path": user_manual_path})


if __name__ == '__main__':
    main()
    #app.run(debug=True)