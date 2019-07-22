from flask import Flask,request,render_template
from flask_wtf import FlaskForm
from wtforms import RadioField,SelectField,SelectMultipleField, SubmitField,validators
from random import choices

app = Flask(__name__)
app.secret_key='1234567890'

class TestForm(FlaskForm):
    radio = RadioField('Please chose a opt',choices=[('val1','opt1'),('val2','opt2')],
                       validators=[validators.AnyOf(['val1','val2'],'please chose one')])
    
    select = SelectField('Please select an item',choices=[('chk1','copt1'),('chk2','copt2')],
                        validators=[validators.AnyOf(['chk1','chk2'],'please select one')])
    
    selectMulti = SelectMultipleField('Please select items',choices=[('mchk1','mcopt1'),('mchk2','mcopt2'),('mchk3','mopt3')],
                        validators=[validators.AnyOf([['mchk1','mchk2'],['mchk1','mchk3']],'please select multi')])
    
    submit = SubmitField('提交')
    
@app.route('/',methods=['GET','POST'])
def test():
    form = TestForm()
    ok = False
    if request.method == 'POST':
        if form.validate_on_submit() == False:
            print('error')
        else:
            print('输入成功')
            print(form.radio.data)
            print(form.select.data)
            print(form.selectMulti.data)
            ok = True
            
    return render_template('select.txt',form=form,ok=ok)

if __name__== '__main__':
    app.run(host='0.0.0.0',port='8002')
    
    