def calculate_cha2ds2_vasc_score(age, sex, congestive_heart_failure, hypertension, diabetes, stroke, vascular_disease):
    score = 0
    
    # Assign points based on age
    if age >= 75:
        score += 2
    elif age >= 65:
        score += 1
    
    # Assign points based on sex (Female: 1 point)
    if sex == 'F':
        score += 1
    
    # Assign points for comorbidities
    if congestive_heart_failure:
        score += 1
    if hypertension:
        score += 1
    if diabetes:
        score += 1
    
    # Assign points for previous stroke or transient ischemic attack (TIA)
    if stroke:
        score += 2
    
    # Assign points for presence of vascular disease
    if vascular_disease:
        score += 1
    
    return score


# Example usage
age = 70
sex = 'M'
congestive_heart_failure = True
hypertension = True
diabetes = False
stroke = True
vascular_disease = False

score = calculate_cha2ds2_vasc_score(age, sex, congestive_heart_failure, hypertension, diabetes, stroke, vascular_disease)
print(f"CHA2DS2-VASc Score: {score}")
