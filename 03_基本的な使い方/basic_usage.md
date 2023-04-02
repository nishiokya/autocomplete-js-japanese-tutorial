# 基本的な使い方
このセクションでは、autoComplete.jsを使用して、基本的な自動補完機能を実装する方法を説明します。

1. ステップ1: HTMLファイルの作成
まず、入力フィールドと提案を表示するためのHTML要素を作成します。

```html

<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <title>autoComplete.js 基本的な使い方</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tarekraafat/autocomplete.js@10.2.7/dist/css/autoComplete.min.css">
<!DOCTYPE html>
<html lang="ja">

  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>autoComplete.js Autocomplete Example</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tarekraafat/autocomplete.js@10.2.3/dist/css/autoComplete.min.css">
    <style>
      input {
        width: 100%;
      }

    </style>
  </head>

  <body>
    <input type="text" id="autoComplete">
    <script src="https://cdn.jsdelivr.net/npm/@tarekraafat/autocomplete.js@10.2.7/dist/autoComplete.min.js"></script>

  </body>

</html>

```

# ステップ2: autoComplete.jsとスタイルシートのインポート

autoComplete.jsをインポートし、HTMLファイルで利用できるようにします。公式CDNから直接読み込むか、自分のプロジェクトにダウンロードして使用してください。




```html
<head>
    ...
    <script src="https://cdn.jsdelivr.net/npm/@tarekraafat/autocomplete.js@10.2.7/dist/autoComplete.min.js"></script>
</head>
```

# ステップ3: autoCompleteインスタンスの作成
次に、autoCompleteインスタンスを作成し、必要な設定を行います。

```javascript
const autoCompleteJS = new autoComplete({
  placeHolder: "Search for Food...",
  data: {
    src: [
      "豚骨ラーメン",
      "醤油ラーメン",
      "味噌ラーメン",
      "塩ラーメン",
      "つけ麺",
      "博多ラーメン",
      "札幌ラーメン",
      "東京ラーメン",
      "熊本ラーメン",
      "鹿児島ラーメン",
      "担々麺",
      "冷やし中華",
      "Tonkotsu Ramen",
      "Shoyu Ramen",
      "Miso Ramen",
      "Shio Ramen",
      "Tsukemen",
      "Hakata Ramen",
      "Sapporo Ramen",
      "Tokyo Ramen",
      "Kumamoto Ramen",
      "Kagoshima Ramen",
      "Tantanmen",
      "Hiyashi Chuka"
    ],
    cache: true,
  },
  resultItem: {
    highlight: true
  },
  events: {
    input: {
      selection: (event) => {
        const selection = event.detail.selection.value;
        autoCompleteJS.input.value = selection;
      }
    }
  }
});
```
これで、基本的なautoComplete.jsの使い方が完了しました。入力フィールドにテキストを入力すると、一致する候補が提案リストに表示されます。なお、autoComplete.jsはCSSスタイルシートを含んでいるため、追加のスタイル設定は不要です。


### 動作確認
https://nishiokya.github.io/autocomplete-js-japanese-tutorial/03_基本的な使い方/examples/basic_example.html