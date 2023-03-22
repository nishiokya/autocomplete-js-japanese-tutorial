ソース
autoComplete.jsでは、様々なデータソースを使用して自動補完候補を提供できます。このセクションでは、いくつかの一般的なデータソースの使用方法について説明します。

## 配列
配列を使用して、候補を直接指定することができます。以下の例では、配列内のオブジェクトがラーメンの名称、読み、ローマ字を含むデータソースとして使用されています。


上記の例では、静的な配列を使用して、ラーメンのデータセットを提供しています。`key`オプションを設定することで、検索対象とするオブジェクトのプロパティを指定しています。

## 外部APIからのデータ取得

外部APIを使用して、動的に候補を提供することもできます。これは、大規模なデータセットやリアルタイムな情報を取得する際に便利です。

以下の例では、外部APIを使用して候補を取得しています。

```javascript

これで、オートコンプリート機能が実装された独自のデータソースを持つautoComplete.jsのチュートリアルが完成です。上記のコードを使用して、独自のデータソースに応じたオートコンプリート機能を実装できます。

また、APIやデータベースからデータを取得する場合は、`data.src`でPromiseを返す関数を指定し、非同期でデータを取得することができます。

```javascript
const fetchApiData = async (query) => {
  const response = await fetch(`https://your-api-endpoint.com/search?q=${query}`);
  const data = await response.json();
  return data;
};

const autoCompleteInstance = new autoComplete({
  // ...
  data: {
    src: (query) => fetchApiData(query),
    key: ["name"],
    cache: false
  },
  // ...
});
```

これで、APIやデータベースから非同期でデータを取得してオートコンプリートを実装することができます。