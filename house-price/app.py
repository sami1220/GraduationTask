from flask import Flask, render_template, request, flash
from wtforms import Form, FloatField, StringField, SubmitField, validators, ValidationError
import numpy as np
import joblib
import pandas as pd
import data_conversion

# 学習済みモデルを読み込み利用
def predict(df):
    # 学習したLightGBMのモデルを読み込み
    model = joblib.load('pickle/lgbm_model.pickle')
    pred = model.predict(df)
    return pred

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'zJe09C5c3tMf5FnNL09C5d6SAzZoY'

class HousePrice(Form):
    #strで入力
    Prefecture = StringField("都道府県名",
                     [validators.InputRequired("この項目は入力必須です")])

    #strで入力
    CityTown  = StringField("市区町村名",
                     [validators.InputRequired("この項目は入力必須です")])

    #strで入力
    District = StringField("地区名",
                     [validators.InputRequired("この項目は入力必須です")])

    #strで入力
    Floor  = StringField("間取り",
                     [validators.InputRequired("この項目は入力必須です")])

    #floatで入力(100平米以内)
    Roomsize  = FloatField("面積（㎡）",
                     [validators.InputRequired("この項目は入力必須です"),
                     validators.NumberRange(min=0, max=100)])

    #strで入力
    Bldplan  = StringField("建物の構造",
                     [validators.InputRequired("この項目は入力必須です")])

    #strで入力
    BldAge  = StringField("建築年",
                     [validators.InputRequired("この項目は入力必須です")])

    # html側で表示するsubmitボタンの表示
    submit = SubmitField("判定")

@app.route('/', methods = ['GET', 'POST'])
def predicts():
    form = HousePrice(request.form)
    if request.method == 'POST':
        if form.validate() == False:
            flash("全て入力する必要があります。")
            return render_template('index.html', form=form)
        else:
            # 全て入力ができている場合以下のように変換
            Prefecture = str(request.form["Prefecture"])
            CityTown = str(request.form["CityTown"])
            District = str(request.form["District"])
            Floor = str(request.form["Floor"])
            Roomsize = float(request.form["Roomsize"])
            Bldplan = str(request.form["Bldplan"])
            BldAge = str(request.form["BldAge"])

            x_df = pd.DataFrame({'都道府県名':[Prefecture],
                                '市区町村名':[CityTown],
                                '地区名':[District],
                                '間取り':[Floor],
                                '面積（㎡）':[Roomsize],
                                '建物の構造':[Bldplan],
                                '建築年':[BldAge]})

            val_df = data_conversion.change_df(x_df)                    

            pred = predict(val_df)
            price = np.exp(pred).astype(int)[0]#対数変換を戻す

            return render_template('result.html', price=price)
    elif request.method == 'GET':

        return render_template('index.html', form=form)

if __name__ == "__main__":
    app.run()