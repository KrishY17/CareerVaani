import numpy as np

# Function to perform SWOT analysis
def swot_analysis(scores):
    # Check if the input array has 8 elements
    if len(scores) != 8:
        return "Input array 'scores' must contain 8 elements (7 subject scores + total marks)."

    # Extract subject scores and total marks
    math_score, physics_score, chemistry_score, biology_score, arts_humanities_score, law_score, commerce_score, total_marks = scores

    # Define the maximum score for each subject (42 marks)
    max_score = 42

    # Calculate percentage scores for each subject
    math_percentage = (math_score / max_score) * 100
    physics_percentage = (physics_score / max_score) * 100
    chemistry_percentage = (chemistry_score / max_score) * 100
    biology_percentage = (biology_score / max_score) * 100
    arts_humanities_percentage = (arts_humanities_score / max_score) * 100
    law_percentage = (law_score / max_score) * 100
    commerce_percentage = (commerce_score / max_score) * 100

    # Strengths (S)
    strengths = []
    if math_percentage >= 90:
        strengths.append("Excellent in Mathematics")
    if physics_percentage >= 90:
        strengths.append("Excellent in Physics")
    if chemistry_percentage >= 90:
        strengths.append("Excellent in Chemistry")
    if biology_percentage >= 90:
        strengths.append("Excellent in Biology")
    if(len(strengths)==0):
        strengths.append("No strengths identified") 


    # Weaknesses (W)
    weaknesses = []
    if math_percentage < 60:
        weaknesses.append("Needs Improvement in Mathematics")
    if physics_percentage < 60:
        weaknesses.append("Needs Improvement in Physics")
    if chemistry_percentage < 60:
        weaknesses.append("Needs Improvement in Chemistry")
    if biology_percentage < 60:
        weaknesses.append("Needs Improvement in Biology")
    if(len(weaknesses)==0):
        weaknesses.append("No weaknesses identified") 

    # Opportunities (O)
    opportunities = []
    if total_marks >= 80:
        opportunities.append("Opportunity to Pursue Higher Education")
    if arts_humanities_percentage >= 80:
        opportunities.append("Opportunity in Arts & Humanities")
    if law_percentage >= 80:
        opportunities.append("Opportunity in Law")
    if commerce_percentage >= 80:
        opportunities.append("Opportunity in Commerce")
    if(len(opportunities)==0):
        opportunities.append("No opportunities identified") 

    # Threats (T)
    threats = []
    if total_marks < 60:
        threats.append("Threat to Academic Progress")
    if arts_humanities_percentage < 60:
        threats.append("Limited Opportunity in Arts & Humanities")
    if law_percentage < 60:
        threats.append("Limited Opportunity in Law")
    if commerce_percentage < 60:
        threats.append("Limited Opportunity in Commerce")
    if(len(threats)==0):
        threats.append("No threats identified") 

    # Create a SWOT analysis report
    swot_report = [strengths,weaknesses,opportunities,threats]
        
    return swot_report


