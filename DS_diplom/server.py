from flask import Flask, request, jsonify
import pickle
import seaborn as sns
import matplotlib.pyplot as plt 

app = Flask(__name__)

# Производим десериализацию и извлекаем модель из файла формата pkl
with open('DS_diplom\my_data_short.pkl', 'rb') as pkl_file:
    data_short = pickle.load(pkl_file)

with open('DS_diplom\my_data.pkl', 'rb') as pkl_file:
    data = pickle.load(pkl_file)

with open('DS_diplom\my_pipeline.pkl', 'rb') as pkl_file:
    my_pipeline = pickle.load(pkl_file)

@app.route('/')
def index():
    msg = "Test message. The server is running"
    return msg

@app.route('/plot', methods = ['POST'])
def plot():
  feature = request.json.get('feature')
  df = data.groupby('label')[feature].mean()
  fig = plt.figure(figsize=(7, 6))
  df.plot(
    kind='bar',
    grid=True,
    figsize=(5, 4),
    colormap='plasma',
    title= f'График распределения признака {feature}',
    rot=0,
    xlabel="Кластеры",
    ylabel= f'Показатель {feature}'
  );
  plt.savefig('DS_diplom\output\plot.png')
  plt.clf()
    
  return jsonify({'result': 'Приложение выполнило задачу!'})


if __name__ == '__main__':

    app.run('localhost', 5000)