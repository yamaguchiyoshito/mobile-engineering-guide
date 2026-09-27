---
title: "入力とバリデーション"
description: "入力とバリデーションの基準と使い方。モバイルアプリ開発の習熟度評価・チーム改善ガイド。"
---

# 入力とバリデーション

**要素技術ID：** `mobile.input-validation`  
**技術領域：** [フレームワーク・実装領域](index.md)  
**対象プラットフォーム：** 共通  
**主な前提：** UI実装

[習熟度の共通定義と判定方法](../../guide/individual-assessment.md)に沿って、根拠を確認します。

## この要素技術について

文字や数値を入力する欄、画面に表示されるキーボード、入力値の検査と誤りの伝え方をまとめて扱う技術です。モバイルアプリでは、画面の下半分をキーボードが覆って入力欄や送信ボタンが隠れることがあり、入力内容に合ったキーボード（数字用、メールアドレス用など）を出すかどうかで入力のしやすさが大きく変わります。最初に押さえるのは、入力の種類に応じたキーボードの指定と、どの項目の何が誤りかを利用者に分かる形で示すエラー表示です。

分からない用語は[用語集](../../guide/glossary.md)で確認できます。

## Lv0

入力欄、キーボード、入力値、エラー表示の関係を説明できず、単純な入力画面の変更にも手順ごとの指示が必要である。

## Lv1

例に沿って入力欄、キーボードの種別、基本的な必須チェックとエラー表示を実装できる。指定された入力と操作で動作を確認できる。

## Lv2

標準的な登録・編集画面で、入力内容に合ったキーボード、次の項目へのフォーカス移動、キーボードによる隠れの回避を実装できる。項目別と全体の検証、送信中と失敗の表示、二重送信の抑制を扱い、複数の画面サイズで検証・修正できる。

## Lv3

項目間の依存、書式の自動整形、複数ステップ、入力途中の保持と復帰、外部キーボードや読み上げ機能での操作を設計できる。端末やOSによる入力挙動の差を分析し、他者の実装をレビューできる。

## Lv4

入力部品、検証ルール、エラー表示の共通パターンと自動検証を整備できる。他者の利用を支援し、画面ごとの挙動のばらつきや入力に関する不具合の減少を確認できる。

## 次のLvへ進むために

学習の目安として、次の段階に進むための課題と参考資料を示します。課題は評価の条件ではありません。

| 目標 | 取り組む課題の例 | 参考資料 |
| :--- | :--- | :--- |
| Lv1 | 名前とメールアドレスの2項目を持つ入力画面を作り、メールアドレス用のキーボードを指定して、空欄のまま送信したときにエラーを表示する | [SwiftUIチュートリアル](https://developer.apple.com/tutorials/swiftui)・[Android Basics with Compose](https://developer.android.com/courses/android-basics-compose/course)・[コアコンポーネント](https://reactnative.dev/docs/intro-react-native-components) |
| Lv2 | 5項目程度の会員登録画面を作り、次の項目へのフォーカス移動、キーボードで隠れない配置、項目ごとの検証、送信中の表示と二重送信の防止を実装する。画面の小さい端末と大きい端末の両方で確認する | [SwiftUI](https://developer.apple.com/documentation/swiftui)・[Jetpack Compose](https://developer.android.com/develop/ui/compose)・[コアコンポーネント](https://reactnative.dev/docs/intro-react-native-components)・[Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines) |
| Lv3 | 電話番号を入力中に自動で区切る処理と、3段階に分かれた入力画面で途中の内容を保持して前の段階に戻れる仕組みを作る。読み上げ機能（VoiceOver／TalkBack）と外部キーボードで操作できることを確認する | [Accessibility](https://developer.apple.com/documentation/accessibility)・[アクセシビリティ（Android）](https://developer.android.com/guide/topics/ui/accessibility)・[アクセシビリティ（React Native）](https://reactnative.dev/docs/accessibility) |

## 技術の対応

| 用途 | iOS | Android | React Native |
| :--- | :--- | :--- | :--- |
| 入力欄 | UITextField／TextField | TextField／EditText | TextInput |
| キーボードの種類と操作 | キーボード種別 | InputType、IMEアクション | keyboardType、returnKeyType |
| キーボードとの重なりとフォーカス | キーボード回避、フォーカス管理 | adjustResize、FocusRequester | KeyboardAvoidingView |
| 検証とエラー表示 | 入力検証とエラー表示、Formatter | 入力検証、エラー表示 | フォームライブラリ（React Hook Form） |

## 関連ライブラリと参考資料

主な一次情報の所在です。掲載は公式資料と、技術の対応表に挙げた広く使われるライブラリに限ります。採用を推奨するものではありません。

<!-- references:start ids="uikit-uitextfield, swiftui-textfield, uikit-uikeyboardtype, uikit-uikeyboardlayoutguide, swiftui-focusstate, foundation-formatter, compose-text-fields, android-edittext, android-input-method-type, android-input-method-visibility, compose-focus, compose-validate-input, rn-textinput, rn-keyboardavoidingview, react-hook-form" -->

| 種別 | 名称 | 対象 | 概要 |
| :--- | :--- | :--- | :--- |
| 公式リファレンス | [UITextField](https://developer.apple.com/documentation/uikit/uitextfield) | iOS | UIKitで1行のテキスト入力を受け付けるコントロール |
| 公式リファレンス | [TextField](https://developer.apple.com/documentation/swiftui/textfield) | iOS | SwiftUIで1行のテキスト入力を受け付けるView |
| 公式リファレンス | [UIKeyboardType](https://developer.apple.com/documentation/uikit/uikeyboardtype) | iOS | 入力欄に表示するキーボードの種類を指定する型 |
| 公式リファレンス | [UIKeyboardLayoutGuide](https://developer.apple.com/documentation/uikit/uikeyboardlayoutguide) | iOS | キーボードの位置に合わせてViewを配置するためのガイド |
| 公式リファレンス | [FocusState](https://developer.apple.com/documentation/swiftui/focusstate) | iOS | 入力欄のフォーカス位置を読み取り・変更するプロパティラッパー |
| 公式リファレンス | [Formatter](https://developer.apple.com/documentation/foundation/formatter) | iOS | 数値や日付などの値と文字列表現を相互に変換する基底クラス |
| 公式リファレンス | [Configure text fields](https://developer.android.com/develop/ui/compose/text/user-input) | Android | ComposeのTextFieldで入力を受け付けて設定する方法 |
| 公式リファレンス | [EditText](https://developer.android.com/reference/android/widget/EditText) | Android | Viewでテキスト入力を受け付ける部品のリファレンス |
| 公式リファレンス | [Specify the input method type](https://developer.android.com/develop/ui/views/touch-and-input/keyboard-input/style) | Android | InputTypeとIMEアクションでキーボードの種類と動作を指定する方法 |
| 公式リファレンス | [Handle input method visibility](https://developer.android.com/develop/ui/views/touch-and-input/keyboard-input/visibility) | Android | キーボードの表示とadjustResizeによる画面調整の扱い方 |
| 公式リファレンス | [Change focus behavior](https://developer.android.com/develop/ui/compose/touch-input/focus/change-focus-behavior) | Android | FocusRequesterなどでフォーカスの移動を制御する方法 |
| 公式リファレンス | [Validate input as the user types](https://developer.android.com/develop/ui/compose/quick-guides/content/validate-input) | Android | 入力中の値を検証してエラーを表示するComposeの実装例 |
| 公式リファレンス | [TextInput](https://reactnative.dev/docs/textinput) | React Native | キーボードからテキスト入力を受け付ける部品 |
| 公式リファレンス | [KeyboardAvoidingView](https://reactnative.dev/docs/keyboardavoidingview) | React Native | キーボードに隠れないように表示位置を調整する部品 |
| ライブラリ | [React Hook Form](https://github.com/react-hook-form/react-hook-form) | React Native | フックでフォームの入力値と検証を管理するライブラリ |

<!-- references:end -->

## 評価を記録する

[個人の習熟度評価書式](../../templates/individual-assessment.md)に、現在の判定、根拠、支援と制約、次の到達条件を記録します。
