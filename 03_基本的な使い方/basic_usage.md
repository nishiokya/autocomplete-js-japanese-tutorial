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
</head>
<body>
    <input type="text" id="autoComplete" placeholder="キーワードを入力してください">
    <ul id="suggestion-list">
    </ul>
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
<script>
    const data = [
        {name: 'とんこつラーメン', kana: 'とんこつらーめん', romaji: 'tonkotsu ramen'},
        {name: 'しょうゆラーメン', kana: 'しょうゆらーめん', romaji: 'shoyu ramen'},
        {name: 'みそラーメン', kana: 'みそらーめん', romaji: 'miso ramen'},
        {name: 'しおラーメン', kana: 'しおらーめん', romaji: 'shio ramen'},
        {name: 'つけ麺', kana: 'つけめん', romaji: 'tsukemen'},
        {name: '担々麺', kana: 'たんたんめん', romaji: 'tantanmen'},
        {name: '坦々麺', kana: 'たんたんめん', romaji: 'tantanmen'},
        {name: '油そば', kana: 'あぶらそば', romaji: 'abura soba'},
        {name: '味噌担々麺', kana: 'みそたんたんめん', romaji: 'miso tantanmen'},
        {name: 'ねぎラーメン', kana: 'ねぎらーめん', romaji: 'negi ramen'}
    ];

    new autoComplete({
        selector: '#autocomplete-input',
        data: {
            src: data,
            key: ['name', 'kana', 'romaji'],
        },
        resultsList: {
            render: true,
            container: () => document.getElementById('suggestion-list'),
            destination: document.getElementById('autocomplete-input'),
            position: 'afterend',
            element: 'ul',
        },
        resultItem: {
            content: (data, element) => {
                element.innerHTML = data.match;
            },
            element: 'li',
        },
        threshold: 1,
    });
</script>
```
これで、基本的なautoComplete.jsの使い方が完了しました。入力フィールドにテキストを入力すると、一致する候補が提案リストに表示されます。なお、autoComplete.jsはCSSスタイルシートを含んでいるため、追加のスタイル設定は不要です。