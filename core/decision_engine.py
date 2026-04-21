def analyze_meal(meal_data):
    """
    Analyzes a meal based on goals, budget, and living mode.
    Returns a dictionary with analysis, suggestions, warnings, and improvements.
    """
    meal_text = meal_data.get('meal', '').lower()
    goal = meal_data.get('goal', 'general_health')
    budget = meal_data.get('budget', 'medium')
    mode = meal_data.get('mode', 'home')

    result = {
        'analysis': "Analyzing your meal...",
        'suggestions': [],
        'warnings': [],
        'improvements': [],
        'health_score': 100  # Base score
    }

    # Basic Food Database (Keywords)
    proteins = ['chicken', 'egg', 'paneer', 'fish', 'tofu', 'dal', 'lentils', 'soy', 'milk', 'curd']
    carbs = ['rice', 'roti', 'bread', 'maggi', 'oats', 'pasta', 'potato', 'burger', 'pizza']
    greens = ['salad', 'vegetables', 'spinach', 'broccoli', 'beans', 'gourd']
    unhealthy = ['maggi', 'burger', 'pizza', 'coke', 'fries', 'chips', 'sugar', 'sweets']

    # 1. Component Check
    has_protein = any(p in meal_text for p in proteins)
    has_carbs = any(c in meal_text for c in carbs)
    has_greens = any(g in meal_text for g in greens)
    is_unhealthy = any(u in meal_text for u in unhealthy)

    # 2. Goal Analysis
    if goal == 'weight_loss':
        if has_carbs and not has_greens:
            result['warnings'].append("High carbohydrate content without fiber (vegetables). This might spike insulin and hinder weight loss.")
            result['health_score'] -= 15
        if is_unhealthy:
            result['warnings'].append("Processed/Fast food detected. High calorie density makes weight loss difficult.")
            result['health_score'] -= 20
        result['suggestions'].append("Try to keep protein high to preserve muscle while losing fat.")
        
    elif goal == 'muscle_gain':
        if not has_protein:
            result['warnings'].append("Missing a strong protein source. Protein is essential for muscle synthesis.")
            result['health_score'] -= 25
        if not has_carbs:
            result['suggestions'].append("Consider adding more complex carbs for energy during workouts.")
        result['suggestions'].append("Ensure you are in a slight calorie surplus.")

    # 3. Budget & Mode Specifics
    if budget == 'low':
        if mode == 'hostel':
            result['improvements'].append("Hostel Hack: Add 2 boiled eggs (cheap & easy protein) or a banana for potassium.")
        else:
            result['improvements'].append("Budget Tip: Use seasonal vegetables and dal for a complete, low-cost amino acid profile.")
    
    if budget == 'high' and is_unhealthy:
        result['suggestions'].append("With your budget, consider switching to premium whole foods like Salmon or Quinoa.")

    # 4. General Logic
    if not has_greens:
        result['warnings'].append("Micronutrient alert: No significant source of vegetables/fiber found in this meal.")
        result['improvements'].append("Add a side of salad or 100g of steamed vegetables.")
        result['health_score'] -= 10

    if is_unhealthy:
        result['analysis'] = f"This meal seems to be a 'cheat meal' or high in processed ingredients."
    elif has_protein and has_greens and has_carbs:
        result['analysis'] = "Excellent! This looks like a well-balanced 'Power Meal'."
        result['health_score'] += 15
    else:
        result['analysis'] = "This is a basic meal. There is room for optimization to meet your goals."

    # Clamp Score
    result['health_score'] = max(10, min(100, result['health_score']))

    return result
