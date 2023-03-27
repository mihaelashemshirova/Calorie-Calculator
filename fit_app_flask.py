from flask import Flask, request
from calorie_calculator_program import CalorieCalculator, Women, Men
app = Flask(__name__)


@app.route('/')
def home():
    return '''
    <head>
    <style>
        body {
           background-color: #bae8e8;
        }
        h1 { 
           color: #272343;
           text-align: center;
           font-family: Arial, Helvetica, sans-serif;
        } 
        h3 {
           text-align: center;
           font-family: Arial, Helvetica, sans-serif;
        }
        p { 
           margin-left: 20px;
           text-align: center;
           font-family: Arial, Helvetica, sans-serif;
           font-style: italic;
        }
        form {
           border-style: groove;
           border-radius: 12px;
           padding: 5px;
           margin: auto;
           width: 50%;
           background-color: #e3f6f5;   
        }
        button {
           background-color: SkyBlue; 
           border: 1px solid blue;
           color: black;
           padding: 15px 32px;
           text-align: center;
           display: inline-block;
           font-size: 16px;
           border-radius: 8px;
        }
        .button:hover {
           background-color: SteelBlue;
        }
    </style>
    </head>
    <body>
        <h1>Калориен калкулатор</h1>
        <form action="/result" method="post">
            <h3>Твоите данни:</h3>	
            <p>Пол
             <input type="radio" id="women" name="gender" value="women">
             <label for="women">жена</label>
             <input type="radio" id="men" name="gender" value="men">
             <label for="men">мъж</label>
            </p>	
            <p>Години <input type="number" name="age" /></p>	
            <p>Тегло в кг <input type="number" name="weight" /></p>	
            <p>Височина в см <input type="number" name="height" /></p>	
            <p>Обиколка 3 см над пъпа <input type="number" name="girth_above_navel" /></p>	
            <p>Обиколка през пъпа <input type="number" name="girth_through_navel" /></p>
            <p>Обиколка ханш в см <input type="number" name="hips" /></p>
            <p>Обиколка врат в см <input type="number" name="neck" /></p>
            <p>Активност	
                <select name="activity">	
                    <option value="1.2">Тренирам рядко или изобщо не тренирам</option>
                    <option value="1.375">Тренирам 2-3 дни седмично</option>
                    <option value="1.55">Тренирам 4-5 дни седмично</option>
                    <option value="1.725">Тренирам 6-7 дни седмично</option>
                    <option value="1.9">Тренирам два пъти дневно всеки ден</option>
                </select>	
            </p>
            <p>Калориен прием 	
                <select name="deficit_surplus">	
                    <option value="-25">25% дефицит</option>
                    <option value="-20">20% дефицит</option>
                    <option value="-15">15% дефицит</option>
                    <option value="0">без дефицит/излишък</option>
                    <option value="+15">15% излишък</option>
                    <option value="+20">20% излишък</option>
                    <option value="+25">25% излишък</option>
                    
                </select>	
            </p>
            <p><button class="button" type="submit">Изчисли</button></p>
        </form>
    </body>
    '''


@app.route('/result', methods=['POST'])
def result():

    global body_fat_per, body_fat_kg, body_weight, basal_metabolism, daily_cal_optimum, daily_fluid_intake, caloric_intake_in_deficit

    gender = request.form['gender']
    age = int(request.form['age'])
    weight = float(request.form['weight'])
    height = int(request.form['height'])
    girth_above_navel = int(request.form['girth_above_navel'])
    girth_through_navel = int(request.form['girth_through_navel'])
    hips = int(request.form['hips'])
    neck = int(request.form['neck'])
    activity = float(request.form['activity'])
    deficit_surplus = int(request.form['deficit_surplus'])

    if gender == 'women':

        ccp = Women(gender, age, weight, height, girth_above_navel, girth_through_navel, hips, neck,
                                activity, deficit_surplus)

        body_fat_per = Women.body_fat_percent(ccp)
        body_fat_kg = Women.body_fat_kg(ccp)
        body_weight = Women.body_weight(ccp)
        basal_metabolism = Women.basal_metabolism(ccp)
        daily_cal_optimum = Women.daily_caloric_optimum(ccp)
        daily_fluid_intake = Women.daily_fluid_intake(ccp)
        caloric_intake_in_deficit = Women.caloric_intake_in_deficit(ccp)

    elif gender == 'men':

        ccp = Men(gender, age, weight, height, girth_above_navel, girth_through_navel, hips, neck,
                                activity, deficit_surplus)

        body_fat_per = Men.body_fat_percent(ccp)
        body_fat_kg = Men.body_fat_kg(ccp)
        body_weight = Men.body_weight(ccp)
        basal_metabolism = Men.basal_metabolism(ccp)
        daily_cal_optimum = Men.daily_caloric_optimum(ccp)
        daily_fluid_intake = Men.daily_fluid_intake(ccp)
        caloric_intake_in_deficit = Men.caloric_intake_in_deficit(ccp)

    return f'''	
          <h1>Резултати:</h1>	
          <p>Телесни мазнини в %: {body_fat_per:.1f}%</p>	
          <p>Телесни мазнини в кг: {body_fat_kg:.1f} кг</p>	
          <p>Активно тегло: {body_weight:.1f} кг</p>	
          <p>Базов метаболизъм (BMR): {int(basal_metabolism)} kcal</p>	
          <p>Дневен калориен оптимум: {int(daily_cal_optimum)} kcal</p>	
          <p>Калориен прием с дефицит/излишък: {int(caloric_intake_in_deficit)} kcal</p>	
          <p>Препоръчителен дневен прием на течности: {daily_fluid_intake}</p>		
      '''


if __name__ == '__main__':
    app.run()
