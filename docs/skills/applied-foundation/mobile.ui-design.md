---
title: "UIデザイン原則とローカライズ"
description: "UIデザイン原則とローカライズの基準と使い方。モバイルアプリ開発の習熟度評価・チーム改善ガイド。"
---

# UIデザイン原則とローカライズ

**要素技術ID：** `mobile.ui-design`  
**技術領域：** [応用基礎領域](index.md)  
**対象プラットフォーム：** 共通  
**主な前提：** モバイル基礎

[習熟度の共通定義と判定方法](../../guide/individual-assessment.md)に沿って、根拠を確認します。

## この要素技術について

アプリの画面を、各OSの見た目と操作の慣習に合わせ、さまざまな画面の大きさや言語でも崩れないように組み立てるための技術です。AppleとGoogleはそれぞれデザインの指針を公開しており、それに沿うことで利用者が慣れた操作で使えます。また、画面の切り欠きやホームバーを避けた表示領域（安全領域）への配慮が必要です。ストアを通じて多くの国に配布できるため、画面の文字列はコードに直接書かず、言語ごとに差し替えられる形で管理します（ローカライズ）。最初に押さえるのは、プラットフォームのデザインガイドライン、安全領域、文字列リソースの3つの考え方です。

分からない用語は[用語集](../../guide/glossary.md)で確認できます。

## Lv0

各プラットフォームのデザインガイドライン、画面サイズや安全領域への対応、文字列をローカライズする必要性を説明できず、画面を組むには手順ごとの指示が必要である。

## Lv1

デザインと例に沿ってレイアウトを組み、余白、文字、アイコンを指定どおりに配置できる。支援を受けて文字列をリソースに分け、複数の画面サイズで表示を確認できる。

## Lv2

プラットフォームのガイドラインに沿って、画面サイズ、向き、安全領域、画面密度、ダークモードに対応したレイアウトを実装できる。文字列をローカライズできる形で管理し、長い訳文、複数形、日付・数値の書式で表示が崩れないことを検証できる。

## Lv3

プラットフォームごとの操作慣習とブランド表現の両立、タブレットや右から左へ書く言語への対応を設計できる。表示崩れやガイドラインからの逸脱の原因を分析し、デザイナーと代替案を比較してレビューできる。

## Lv4

デザイントークン、共通レイアウト部品、ローカライズの運用手順、表示確認の自動検証を整備できる。他者の利用結果を基に、表示不具合や翻訳の手戻りの減少を確認し、仕組みを更新できる。

## 次のLvへ進むために

学習の目安として、次の段階に進むための課題と参考資料を示します。課題は評価の条件ではありません。

| 目標 | 取り組む課題の例 | 参考資料 |
| :--- | :--- | :--- |
| Lv1 | 公式チュートリアルに沿ってプロフィール画面を作り、デザインどおりに余白、文字、アイコンを配置する。画面の文字列をリソースに分け、画面の小さい端末と大きい端末のシミュレーターで表示を確認する | [SwiftUIチュートリアル](https://developer.apple.com/tutorials/swiftui)・[Android Basics with Compose](https://developer.android.com/courses/android-basics-compose/course)・[スタイル（React Native）](https://reactnative.dev/docs/style) |
| Lv2 | 設定画面を作り、縦横の向き、ダークモード、日本語と英語の切り替えに対応させる。長い訳文、複数形、日付と数値の書式を入れて表示が崩れないことを確認する | [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines)・[Material Design 3](https://m3.material.io/)・[Flexbox（React Native）](https://reactnative.dev/docs/flexbox) |
| Lv3 | スマートフォン向けの既存画面を、タブレットと右から左へ書く言語に対応させる設計を行う。iOSとAndroidで操作の慣習が異なる箇所（戻る操作、タブの位置など）を洗い出し、ブランド表現と両立する案をデザイナーと比較する | [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines)・[Material Design 3](https://m3.material.io/)・[プラットフォーム固有コード（React Native）](https://reactnative.dev/docs/platform-specific-code) |

## 技術の対応

| 用途 | iOS | Android | React Native |
| :--- | :--- | :--- | :--- |
| デザインの指針とアイコン | Human Interface Guidelines、SF Symbols | Material Design | Platform別スタイル |
| レイアウト | Auto Layout | ConstraintLayout／Composeレイアウト | Flexbox、StyleSheet |
| 画面サイズと安全領域 | Safe Area、Size Class | 画面密度・リソース修飾子 | SafeAreaView |
| ローカライズ | String Catalog | strings.xml、多言語・RTL | i18nライブラリ |

## 関連ライブラリと参考資料

主な一次情報の所在です。掲載は公式資料と、技術の対応表に挙げた広く使われるライブラリに限ります。採用を推奨するものではありません。

<!-- references:start ids="hig, hig-layout, hig-sf-symbols, nslayoutconstraint, uikit-safe-area, string-catalog, material-design-3, constraintlayout, compose-layout, android-screen-densities, android-localization, rn-flexbox, rn-stylesheet, rn-safeareaview, rn-platform-specific-code" -->

| 種別 | 名称 | 対象 | 概要 |
| :--- | :--- | :--- | :--- |
| 公式リファレンス | [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines) | iOS | Appleのプラットフォームで画面や操作を設計するための指針 |
| 公式リファレンス | [Layout（Human Interface Guidelines）](https://developer.apple.com/design/human-interface-guidelines/layout) | iOS | 安全領域やサイズクラスを踏まえて画面を配置するための指針 |
| 公式リファレンス | [SF Symbols（Human Interface Guidelines）](https://developer.apple.com/design/human-interface-guidelines/sf-symbols) | iOS | システムの文字と調和するアイコン群SF Symbolsの使い方 |
| 公式リファレンス | [NSLayoutConstraint](https://developer.apple.com/documentation/uikit/nslayoutconstraint) | iOS | Auto Layoutでビュー同士の位置と大きさの関係を定義する制約 |
| 公式リファレンス | [Positioning content relative to the safe area](https://developer.apple.com/documentation/uikit/positioning-content-relative-to-the-safe-area) | iOS | ほかの表示に隠れないよう安全領域に沿ってビューを置く方法 |
| 公式リファレンス | [Localizing and varying text with a string catalog](https://developer.apple.com/documentation/xcode/localizing-and-varying-text-with-a-string-catalog) | iOS | String Catalogで翻訳や複数形の文字列を管理する方法 |
| 公式リファレンス | [Material Design 3](https://m3.material.io/) | Android | Googleのデザインシステムの設計指針、部品、アイコンの資料 |
| 公式リファレンス | [Build a responsive UI with ConstraintLayout](https://developer.android.com/develop/ui/views/layout/constraint-layout) | Android | 要素同士の制約で位置を決めるViewのレイアウトの使い方 |
| 公式リファレンス | [Compose layout basics](https://developer.android.com/develop/ui/compose/layouts/basics) | Android | Composeで要素を並べて画面を組み立てるレイアウトの基本 |
| 公式リファレンス | [Support different pixel densities](https://developer.android.com/training/multiscreen/screendensities) | Android | 密度に依存しない単位と、画面密度ごとのリソースの用意の仕方 |
| 公式リファレンス | [Localize your app](https://developer.android.com/guide/topics/resources/localization) | Android | strings.xmlなどのリソースで多言語に対応する方法 |
| 公式リファレンス | [Flexbox（React Native）](https://reactnative.dev/docs/flexbox) | React Native | Flexboxで子要素の並ぶ方向、配置、大きさを決める方法 |
| 公式リファレンス | [StyleSheet](https://reactnative.dev/docs/stylesheet) | React Native | 部品のスタイルをオブジェクトとして定義してまとめるAPI |
| 公式リファレンス | [SafeAreaView](https://reactnative.dev/docs/safeareaview) | React Native | iOSの安全領域の内側に内容を描画する部品。現在は非推奨 |
| 公式リファレンス | [Platform-Specific Code（React Native）](https://reactnative.dev/docs/platform-specific-code) | React Native | OSごとに処理やスタイル、ファイルを切り替える方法 |

<!-- references:end -->

roadmap.shで学ぶ：[iOS](https://roadmap.sh/ios)（HIG、UI Design、Auto Layout、Building Interfaces）／[SwiftUI](https://roadmap.sh/swift-ui)（Localization、Font、Padding）／[Android](https://roadmap.sh/android)（Interface & Navigation、ConstraintLayout、Icon、Text）／[React Native](https://roadmap.sh/react-native)（Layouts & Flexbox、Styling、StyleSheets、SafeAreaView、StatusBar）

## 評価を記録する

[個人の習熟度評価書式](../../templates/individual-assessment.md)に、現在の判定、根拠、支援と制約、次の到達条件を記録します。
