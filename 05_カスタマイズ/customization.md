
# Configurationの解説

## Options

|項目名|説明|型|デフォルト値|サンプル値|
|---|---|---|---|---|
|name|インスタンス名|String|autoComplete||
|selector|入力要素を指定するセレクタ|String or Function|autoComplete|selector: () => {<br>    return [Element]; // Any valid selector<br>},|
|wrapper ||Boolean|true||
|data|自動補完のデータソースとキー検索方法を指定,methodと一緒に指定|Object|{src: [}},keys:null}|{src: ['apple', 'banana'], key: ['value']}|
|trigger	|自動補完が開始されるトリガーイベント	|Function	|{ event: ["input"], condition: (query) => query.length >= 1 }|	{ event: ["input"], condition: (query) => query.length >= 3 }|
|query|ユーザー入力を処理する関数|Function|null|(input) => { return input}|
|placeHolder|入力フィールドのプレースホルダーテキスト|String|Blank/Empty|"Type to search"|
|threshold|検索を開始する最小文字数|Integer|1|3|
|debounce|入力間隔を制御するデバウンス時間（ミリ秒）|Integer|0|300|
|searchEngine|検索エンジンのロジックを指定|String or Function|"strict"|"loose" or (query, record) => { return record.value.includes(query)}|
|diacritics|ダイアクリティカルマークを無視するかどうか、「café（カフェ）」を検索する際に、éをeと同じように扱えるようにすることができます。|Boolean|true|false|
|resultsList|検索結果リストの設定|Object or Boolean|{}|{} or false|
|submit|Enterボタンのデフォルト動作|Boolean|false|true|
|events|入力フィールドと結果リストのイベントの追加または上書き|Object|{}|{}|

### data



### resultsList (optional)


### resultItem (optional)
