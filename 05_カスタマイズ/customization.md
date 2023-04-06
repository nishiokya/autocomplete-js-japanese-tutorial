
# Configurationの解説

## Options

| 項目名       | 説明                                                                                                                           | 型                 | デフォルト値                                                  | サンプル値                                                             |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------ | ------------------------------------------------------------- | ---------------------------------------------------------------------- |
| name         | インスタンス名                                                                                                                 | String             | autoComplete                                                  |                                                                        |
| selector     | 入力要素を指定するセレクタ                                                                                                     | String or Function | autoComplete                                                  | selector: () => {<br>    return [Element]; // Any valid selector<br>}, |
| wrapper      |                                                                                                                                | Boolean            | true                                                          |                                                                        |
| data         | 自動補完のデータソースとキー検索方法を指定,methodと一緒に指定                                                                  | Object             | {src: [}},keys:null}                                          | {src: ['apple', 'banana'], key: ['value']}                             |
| trigger      | 自動補完が開始されるトリガーイベント                                                                                           | Function           | { event: ["input"], condition: (query) => query.length >= 1 } | { event: ["input"], condition: (query) => query.length >= 3 }          |
| query        | ユーザー入力を処理する関数                                                                                                     | Function           | null                                                          | (input) => { return input}                                             |
| placeHolder  | 入力フィールドのプレースホルダーテキスト                                                                                       | String             | Blank/Empty                                                   | "Type to search"                                                       |
| threshold    | 検索を開始する最小文字数                                                                                                       | Integer            | 1                                                             | 3                                                                      |
| debounce     | 入力間隔を制御するデバウンス時間（ミリ秒）                                                                                     | Integer            | 0                                                             | 300                                                                    |
| searchEngine | 検索エンジンのロジックを指定                                                                                                   | String or Function | "strict"                                                      | "loose" or (query, record) => { return record.value.includes(query)}   |
| diacritics   | ダイアクリティカルマークを無視するかどうか、「café（カフェ）」を検索する際に、éをeと同じように扱えるようにすることができます。 | Boolean            | true                                                          | false                                                                  |
| resultsList  | 検索結果リストの設定                                                                                                           | Object or Boolean  | {}                                                            | {} or false                                                            |
| submit       | Enterボタンのデフォルト動作                                                                                                    | Boolean            | false                                                         | true                                                                   |
| events       | 入力フィールドと結果リストのイベントの追加または上書き                                                                         | Object             | {}                                                            | {}                                                                     |

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
項目名	説明	型	デフォルト値
content	結果リスト内の各項目をカスタマイズする関数	Function	null
element	結果リスト内の各項目のHTML要素を指定する文字列	String	"li"
idName	結果リスト内の各項目に適用されるID属性の名前	String	"id"
className	結果リスト内の各項目に適用されるCSSクラス名	String	"result-item"
highlight	ユーザーが入力した検索クエリを結果リスト内で強調表示するかどうか	Boolean	false
selected	ユーザーが選択した項目に適用されるCSSクラス名	String	"selected"
maxResults	結果リストに表示される最大結果数	Integer	Infinity


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