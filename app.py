from flask import Flask , render_template, request
from joblib import load
from datetime import datetime
model=load('./savedModels/model.joblib')
app=Flask(__name__)


@app.route("/",methods=['GET'])
def hello():
    return render_template("index.html")

@app.route('/',methods=['POST'])
def predict():
    if request.method == 'POST':
        id=request.form['id']
        entid=request.form['entid']
        founded=datetime.strptime(request.form['founded'], '%Y-%m-%d').year
        if(request.form['closed']==""):
            closed=2021
        else:
            closed=datetime.strptime(request.form['closed'], '%Y-%m-%d').year
        investmentrounds=request.form['investmentrounds']
        fundingrounds=request.form['fundingrounds']
        fundingtotal=request.form['fundingtotal']
        milestones=request.form['milestones']
        relationship=request.form['relationship']
        created=datetime.strptime(request.form['created'], '%Y-%m-%d').year
        updated=datetime.strptime(request.form['updated'], '%Y-%m-%d').year
        roi=request.form['roi']
        age=request.form['age']
        categorycode=request.form['categorycode']
        countrycode=request.form['countrycode']
        
        if(countrycode=='AUS'):
            country_code_AUS=1
            country_code_CAN=0
            country_code_DEU=0
            country_code_ESP=0
            country_code_FRA=0
            country_code_GBR=0
            country_code_IND=0
            country_code_ISR=0
            country_code_NLD=0
            country_code_USA=0
            country_code_other=0
        elif(countrycode=='CAN'):
            country_code_AUS=0
            country_code_CAN=1
            country_code_DEU=0
            country_code_ESP=0
            country_code_FRA=0
            country_code_GBR=0
            country_code_IND=0
            country_code_ISR=0
            country_code_NLD=0
            country_code_USA=0
            country_code_other=0
        elif(countrycode=='DEU'):
            country_code_AUS=0
            country_code_CAN=0
            country_code_DEU=1
            country_code_ESP=0
            country_code_FRA=0
            country_code_GBR=0
            country_code_IND=0
            country_code_ISR=0
            country_code_NLD=0
            country_code_USA=0
            country_code_other=0
        elif(countrycode=='ESP'):
            country_code_AUS=0
            country_code_CAN=0
            country_code_DEU=0
            country_code_ESP=1
            country_code_FRA=0
            country_code_GBR=0
            country_code_IND=0
            country_code_ISR=0
            country_code_NLD=0
            country_code_USA=0
            country_code_other=0 
        elif(countrycode=='FRA'):
            country_code_AUS=0
            country_code_CAN=0
            country_code_DEU=0
            country_code_ESP=0
            country_code_FRA=1
            country_code_GBR=0
            country_code_IND=0
            country_code_ISR=0
            country_code_NLD=0
            country_code_USA=0
            country_code_other=0 
        elif(countrycode=='GBR'):
            country_code_AUS=0
            country_code_CAN=0
            country_code_DEU=0
            country_code_ESP=0
            country_code_FRA=0
            country_code_GBR=1
            country_code_IND=0
            country_code_ISR=0
            country_code_NLD=0
            country_code_USA=0
            country_code_other=0 
        elif(countrycode=='IND'):
            country_code_AUS=0
            country_code_CAN=0
            country_code_DEU=0
            country_code_ESP=0
            country_code_FRA=0
            country_code_GBR=0
            country_code_IND=1
            country_code_ISR=0
            country_code_NLD=0
            country_code_USA=0
            country_code_other=0   
        elif(countrycode=='ISR'):
            country_code_AUS=0
            country_code_CAN=0
            country_code_DEU=0
            country_code_ESP=0
            country_code_FRA=0
            country_code_GBR=0
            country_code_IND=0
            country_code_ISR=1
            country_code_NLD=0
            country_code_USA=0
            country_code_other=0    
        elif(countrycode=='NLD'):
            country_code_AUS=0
            country_code_CAN=0
            country_code_DEU=0
            country_code_ESP=0
            country_code_FRA=0
            country_code_GBR=0
            country_code_IND=0
            country_code_ISR=0
            country_code_NLD=1
            country_code_USA=0
            country_code_other=0  
        elif(countrycode=='USA'):
            country_code_AUS=0
            country_code_CAN=0
            country_code_DEU=0
            country_code_ESP=0
            country_code_FRA=0
            country_code_GBR=0
            country_code_IND=0
            country_code_ISR=0
            country_code_NLD=0
            country_code_USA=1
            country_code_other=0  
        else:
            country_code_AUS=0
            country_code_CAN=0
            country_code_DEU=0
            country_code_ESP=0
            country_code_FRA=0
            country_code_GBR=0
            country_code_IND=0
            country_code_ISR=0
            country_code_NLD=0
            country_code_USA=0
            country_code_other=1
        if(categorycode=='advertising'):
            category_code_advertising=1
            category_code_biotech=0
            category_code_consulting=0
            category_code_ecommerce=0
            category_code_enterprise=0  
            category_code_games_video=0
            category_code_mobile=0
            category_code_other=0
            category_code_software=0
            category_code_web=0
        elif(categorycode=='biotech') :
            category_code_advertising=0
            category_code_biotech=1
            category_code_consulting=0
            category_code_ecommerce=0
            category_code_enterprise=0  
            category_code_games_video=0
            category_code_mobile=0
            category_code_other=0
            category_code_software=0
            category_code_web=0
        elif(categorycode=='consulting') :
            category_code_advertising=0
            category_code_biotech=0
            category_code_consulting=1
            category_code_ecommerce=0
            category_code_enterprise=0  
            category_code_games_video=0
            category_code_mobile=0
            category_code_other=0
            category_code_software=0
            category_code_web=0
        elif(categorycode=='ecommerce') :
            category_code_advertising=0
            category_code_biotech=0
            category_code_consulting=0
            category_code_ecommerce=1
            category_code_enterprise=0  
            category_code_games_video=0
            category_code_mobile=0
            category_code_other=0
            category_code_software=0
            category_code_web=0
        elif(categorycode=='enterprise') :
            category_code_advertising=0
            category_code_biotech=0
            category_code_consulting=0
            category_code_ecommerce=0
            category_code_enterprise=1  
            category_code_games_video=0
            category_code_mobile=0
            category_code_other=0
            category_code_software=0
            category_code_web=0
        elif(categorycode=='videogames') :
            category_code_advertising=0
            category_code_biotech=0
            category_code_consulting=0
            category_code_ecommerce=0
            category_code_enterprise=0  
            category_code_games_video=1
            category_code_mobile=0
            category_code_other=0
            category_code_software=0
            category_code_web=0
        elif(categorycode=='mobile') :
            category_code_advertising=0
            category_code_biotech=0
            category_code_consulting=0
            category_code_ecommerce=0
            category_code_enterprise=0  
            category_code_games_video=0
            category_code_mobile=1
            category_code_other=0
            category_code_software=0
            category_code_web=0
        elif(categorycode=='software') :
            category_code_advertising=0
            category_code_biotech=0
            category_code_consulting=0
            category_code_ecommerce=0
            category_code_enterprise=0  
            category_code_games_video=0
            category_code_mobile=0
            category_code_other=0
            category_code_software=1
            category_code_web=0
        elif(categorycode=='web') :
            category_code_advertising=0
            category_code_biotech=0
            category_code_consulting=0
            category_code_ecommerce=0
            category_code_enterprise=0  
            category_code_games_video=0
            category_code_mobile=0
            category_code_other=0
            category_code_software=0
            category_code_web=1
        else :
            category_code_advertising=0
            category_code_biotech=0
            category_code_consulting=0
            category_code_ecommerce=0
            category_code_enterprise=0  
            category_code_games_video=0
            category_code_mobile=0
            category_code_other=1
            category_code_software=0
            category_code_web=0
        
        y_pred=model.predict([[id,entid,founded,closed,investmentrounds,
        fundingrounds,fundingtotal,milestones,relationship,created,
        updated,roi,age,category_code_advertising,category_code_biotech,
        category_code_consulting,category_code_ecommerce,category_code_enterprise,
        category_code_games_video,category_code_mobile,category_code_other,
        category_code_software,category_code_web,country_code_AUS,
        country_code_CAN,country_code_DEU,country_code_ESP,country_code_FRA,
        country_code_GBR,country_code_IND,country_code_ISR,country_code_NLD,
        country_code_USA,country_code_other]])
        if y_pred[0]==1:
            y_pred='Operating'
        else:
            y_pred='Not Operating'
            
        
    return render_template('index.html',result=y_pred)

    


if __name__=="__main__":
    app.run(debug=True)