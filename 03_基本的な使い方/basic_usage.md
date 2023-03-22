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
   const autoCompleteJS = new autoComplete({
        selector: "#autoComplete",
        placeHolder: "ラーメンの種類を入力してください...",
        data: {
            src: ["しょうゆラーメン",
                "みそラーメン",
                "しおラーメン",
                "とんこつラーメン",
                "つけめん",
                "油そば",
                "担々麺",
                "坦々麺",
                "味噌担々麺",
                "鶏白湯ラーメン",
                "家系ラーメン",
                "二郎系ラーメン",
                "博多ラーメン",
                "札幌ラーメン",
                "熊本ラーメン",],
            cache: true,
        },
        resultsList: {
            element: (list, data) => {
                if (!data.results.length) {
                    // Create "No Results" message element
                    const message = document.createElement("div");
                    // Add class to the created element
                    message.setAttribute("class", "no_result");
                    // Add message text content
                    message.innerHTML = `<span>Found No Results for "${data.query}"</span>`;
                    // Append message element to the results list
                    list.prepend(message);
                }
            },
            noResults: true,
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
</script>
```
これで、基本的なautoComplete.jsの使い方が完了しました。入力フィールドにテキストを入力すると、一致する候補が提案リストに表示されます。なお、autoComplete.jsはCSSスタイルシートを含んでいるため、追加のスタイル設定は不要です。