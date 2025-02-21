from flask import Flask, jsonify, render_template
import random
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

@app.route('/check', methods=['GET'])
def check():
    return jsonify(status="OK")

@app.route('/jason', methods=['GET'])
def jason():
    quotation = random.choice(quotations)
    return render_template('json.html', quotation = quotation)

# Массив с 50 цитатами Стэтхэма
quotations = [
    "Сила – не в бабках. Ведь бабки – уже старые.",
    "Из проведённых 64-х боёв у меня 64 победы. Все бои были с тенью.",
    "Взял нож — режь, взял дошик — ешь.",
    "Никогда не сдавайтесь, идите к своей цели! А если будет сложно – сдавайтесь.",
    "Если заблудился в лесу, иди домой.",
    "Я вообще делаю что хочу. Хочу импланты — звоню врачу.",
    "В жизни всегда есть две дороги: одна — первая, а другая — вторая.",
    "Сниму квартиру. Порядок на районе гарантирую.",
    "Настоящий мужчина, как ковёр тёти Зины – с каждым годом лысеет.",
    "Запомни: всего одна ошибка – и ты ошибся.",
    "Мы должны оставаться мыми, а они – оними.",
    "Делай, как надо. Как не надо, не делай.",
    "Работа — это не волк. Работа — ворк. А волк — это ходить.",
    "Не будьте эгоистами, в первую очередь думайте о себе!",
    "Марианскую впадину знаешь? Это я упал.",
    "Если тебе где-то не рады в рваных носках, то и в целых туда идти не стоит.",
    "Если закрыть глаза, становится темно.",
    "Тут — это вам не там.",
    "Кто рано встаёт — тому весь день спать хочется.",
    "Если вы собираетесь что-то сделать, делайте это стильно!",
]

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)