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

roadmap.shで学ぶ：[iOS](https://roadmap.sh/ios)（User interactions）／[SwiftUI](https://roadmap.sh/swift-ui)（User interaction、UI controls、Form）／[Android](https://roadmap.sh/android)（TextField、TextView）／[React Native](https://roadmap.sh/react-native)（Text input、KeyboardAvoidingView、Gesture handling）

## 評価を記録する

[個人の習熟度評価書式](../../templates/individual-assessment.md)に、現在の判定、根拠、支援と制約、次の到達条件を記録します。
