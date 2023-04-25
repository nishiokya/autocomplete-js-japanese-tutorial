
# Configurationの解説

## Options


機能や見た目をカスタマイズした自動補完機能を実装することができます。
具体的な設定方法やパラメータについては、それぞれの項目の解説を参照してください。
以下に主な設定項目を示します。

| 項目名   | 説明   | 型 | デフォルト値  | サンプル値 |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------ | ------------------------------------------------------------- | ---------------------------------------------------------------------- |
| name  | インスタンスに任意の名前をつけることができます。 | String  | autoComplete   ||
| selector | 入力要素を指定するセレクタを設定できます。 | String or Function | #autoComplete  | selector: () => {<br>return [Element]; // Any valid selector<br>}, |
| wrapper  || Boolean| true  ||
| data |自動補完のデータソースとキー検索方法を指定できます  | Object | {src: [}},keys:null}  | {src: ['apple', 'banana'], key: ['value']} |
| trigger  | 自動補完が開始されるトリガーイベントを設定できます。   | Function   | { event: ["input"], condition: (query) => query.length >= 1 } | { event: ["input"], condition: (query) => query.length >= 3 }  |
| query| 入力フィールドのプレースホルダーテキストを設定できます。 | Function   | null  | (input) => { return input} |
| placeHolder  | 入力フィールドのプレースホルダーテキスト   | String | Blank/Empty   | "Type to search"   |
| threshold| 検索を開始する最小文字数を設定できます。  | Integer| 1 | 3  |
| debounce | 入力間隔を制御するデバウンス時間（ミリ秒）を設定できます。 | Integer| 0 | 300|
| searchEngine | 検索エンジンのロジックを設定できます。 | String or Function | "strict"  | "loose" or (query, record) => { return record.value.includes(query)}   |
| diacritics   | ダイアクリティカルマークを無視するかどうか設定できます。falseにすると「café（カフェ）」を検索する際に、éをeと同じように扱えるようにすることができます。 | Boolean| true  | false  |
| resultsList  | 検索結果リストの設定   | Object or Boolean  | {}| {} or false|
| submit   | Enterボタンのデフォルト動作を設定できます。 Boolean| false | true   |
| events   | 入力フィールドと結果リストのイベントの追加または上書き | Object | {}| {} |



### 設定例


この設定例では、日本のラーメンと一部英語表記のラーメンを検索する自動補完機能が実装されています。

```javascript
const autoCompleteJS = new autoComplete({
  name: "autoComplete",
  selector: "#autoComplete",
  wrapper: true,
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
  trigger: (query) => {
    return query.replace(/ /g, "").length > 0; // スペースを無視する
  },
  query: (input) => {
    return input.replace("lamen", "ラーメン");
  },
  placeHolder: "検索クエリを入力してください...",
  threshold: 2,
  debounce: 300, // Milliseconds value
  searchEngine: "loose",
  diacritics: true,
  resultItem: {
    highlight: true
  },
  submit: true,
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
この設定により、ラーメンの種類を検索しやすくする自動補完機能が実現されています。例えば、"lamen"と入力された場合でも"ラーメン"として検索結果が表示されるようになっています。また、検索結果の一致部分がハイライトされているため、ユーザーが求めている情報をすぐに見つけられるようになっています。
### data

| 項目名                                  | 説明                                                                                           | 型                                                         | サンプル値 |
| --------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------- | ---------- |
| rc	自動補完の候補データソースを提供する | 配列、オブジェクト、JSONまたはAPI	Array, Object, JSON, API                                     | ['apple', 'banana'], [{value: 'apple'}, {value: 'banana'}] |
| keys                                    | データソースがオブジェクトの場合、検索対象となるプロパティ名を指定するキーの配列	Array or null | ['value']                                                  |
| cache                                   | キャッシュを有効にして、以前の検索結果を保存し、同じ検索クエリに対して高速に結果を表示する     | Boolean                                                    | true       |

```javascript
const autoCompleteJS = new autoComplete({
  data: {
    src: [
      { value: "apple", category: "fruit" },
      { value: "banana", category: "fruit" },
      { value: "carrot", category: "vegetable" },
      { value: "broccoli", category: "vegetable" }
    ],
    keys: ["value"],
    cache: true
  },
}

autoCompleteJS.init();
```

### resultsList (optional)

| 項目名      | 説明                                                     | 型                  | サンプル値           |
| ----------- | -------------------------------------------------------- | ------------------- | -------------------- |
| id    | 検索結果リスト要素のID名                                 | String              | "auto_complete_list" |
| class   | 検索結果リスト要素のクラス名                             | 
| className   | 検索結果リスト要素のクラス名                             | String              | "auto_complete_list" |String              | "auto_complete_list" |
| destination | 検索結果リストが挿入される要素を指定するセレクタ         | String or Function  | null                 |
| position    | 検索結果リストの表示位置 (inputの前後)                   | String              | "afterend"           |
| element     | 検索結果リストのHTML要素タイプ                           | String              | "ul"                 |
| maxResults  | 表示する検索結果の最大数                                 | Integer             | 5                    |
| noResults   | 該当する検索結果がない場合に表示するメッセージまたはHTML | Boolean or Function | false                |
| highlight   | 検索結果の一致する部分をハイライトするかどうか           | Boolean             | false                |
| resultItem  | 検索結果アイテムの設定	 |Object	 |{}                         |
| navigation  | 検索結果リストのナビゲーション設定	 |Object |	{}             |
| container   | 検索結果リストのコンテナ要素をカスタマイズする関数       | Function            | null                 |

```javascript
{
resultsList: {
    container: (source) => { return source.setAttribute("id", "custom_container"); },
    destination: "#input-field",
    position: "afterend",
    element: "ul",
    idName: "custom_id",
    className: "custom_class",
    maxResults: 10,
    noResults: (dataFeedback, generateList) => {
        generateList(dataFeedback, "No results found");
    },
    highlight: true,
    resultItem: {
        content: (data, source) => {
            source.innerHTML = data.match;
        },
        element: "li",
    },
    navigation: {
        next: "ArrowDown",
        prev: "ArrowUp",
        esc: "Escape",
        enter: "Enter",
    },
    }
}
```

### resultItem (optional)

検索結果アイテムの設定	

| 項目名                                  | 説明                                                                                           | 型                                                         | サンプル値 |
| --------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------- | ---------- |
|content|	結果リスト内の各項目をカスタマイズする関数|	Function	|null|
|element	|結果リスト内の各項目のHTML要素を指定する文字列	|String	|"li"|
|idName	|結果リスト内の各項目に適用されるID属性の名前	|String	|"id"|
|className	|結果リスト内の各項目に適用されるCSSクラス名	|String	|"result-item"|
|highlight	|ユーザーが入力した検索クエリを結果リスト内で強調表示するかどうか	|Boolean	|false|
|selected	|ユーザーが選択した項目に適用されるCSSクラス名	|String	"selected"|
|maxResults	|結果リストに表示される最大結果数|	Integer	|Infinity|



```javascript
resultsList: {
  container: (source) => {
    source.setAttribute("id", "custom-results-list");
  },
  destination: "#custom-input-field",
  position: "afterend",
  element: "ul",
  idName: "custom-id",
  className: "custom-results-list",
  maxResults: 10,
  navigation: true
}
```