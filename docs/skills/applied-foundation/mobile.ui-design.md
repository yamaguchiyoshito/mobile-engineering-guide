---
title: "UIデザイン原則とローカライズ"
description: "UIデザイン原則とローカライズの基準と使い方。モバイルアプリ開発のスキル評価・チーム改善ガイド。"
---

# UIデザイン原則とローカライズ

**スキルID：** `mobile.ui-design`  
**スキル領域：** [応用基礎領域](index.md)  
**対象プラットフォーム：** 共通  
**主な前提：** モバイル基礎

[習熟度の共通定義と判定方法](../../guide/individual-assessment.md)に沿って、根拠を確認します。

## このスキルについて

アプリの画面を、各 OS の見た目と操作の慣習に合わせ、さまざまな画面の大きさや言語でも崩れないように組み立てるためのスキルです。Apple と Google はそれぞれデザインの指針を公開しており、それに沿うことで利用者が慣れた操作で使えます。また、画面の切り欠きやホームバーを避けた表示領域（安全領域）への配慮が必要なほか、ストアを通じて多くの国に配布できるため、画面の文字列をコードに直接書かず言語ごとに差し替えられる形で管理します（ローカライズ）。最初に押さえるのは、プラットフォームのデザインガイドライン、安全領域、文字列リソースの3つの考え方です。

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
| Lv1 | 公式チュートリアルに沿ってプロフィール画面を作り、デザインどおりに余白、文字、アイコンを配置する。画面の文字列をリソースに分け、画面の小さい端末と大きい端末のシミュレーターで表示を確認する | [SwiftUI チュートリアル](https://developer.apple.com/tutorials/swiftui)・[Android Basics with Compose](https://developer.android.com/courses/android-basics-compose/course)・[スタイル（React Native）](https://reactnative.dev/docs/style) |
| Lv2 | 設定画面を作り、縦横の向き、ダークモード、日本語と英語の切り替えに対応させる。長い訳文、複数形、日付と数値の書式を入れて表示が崩れないことを確認する | [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines)・[Material Design 3](https://m3.material.io/)・[Flexbox（React Native）](https://reactnative.dev/docs/flexbox) |
| Lv3 | スマートフォン向けの既存画面を、タブレットと右から左へ書く言語に対応させる設計を行う。iOS と Android で操作の慣習が異なる箇所（戻る操作、タブの位置など）を洗い出し、ブランド表現と両立する案をデザイナーと比較する | [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines)・[Material Design 3](https://m3.material.io/)・[プラットフォーム固有コード（React Native）](https://reactnative.dev/docs/platform-specific-code) |

## 技術の対応

| 用途 | iOS | Android | React Native |
| :--- | :--- | :--- | :--- |
| デザインの指針とアイコン | Human Interface Guidelines、SF Symbols | Material Design | Platform 別スタイル |
| レイアウト | Auto Layout | ConstraintLayout／Compose レイアウト | Flexbox、StyleSheet |
| 画面サイズと安全領域 | Safe Area、Size Class | 画面密度・リソース修飾子 | SafeAreaView |
| ローカライズ | String Catalog | strings.xml、多言語・RTL | i18n ライブラリ |

roadmap.sh で学ぶ：[iOS](https://roadmap.sh/ios)（HIG、UI Design、Auto Layout、Building Interfaces）／[SwiftUI](https://roadmap.sh/swift-ui)（Localization、Font、Padding）／[Android](https://roadmap.sh/android)（Interface & Navigation、ConstraintLayout、Icon、Text）／[React Native](https://roadmap.sh/react-native)（Layouts & Flexbox、Styling、StyleSheets、SafeAreaView、StatusBar）

## 評価を記録する

[個人のスキル評価書式](../../templates/individual-assessment.md)に、現在の判定、根拠、支援と制約、次の到達条件を記録します。
