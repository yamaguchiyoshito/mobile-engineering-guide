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

## 技術の対応

| プラットフォーム | 主な技術・API |
| :--- | :--- |
| iOS | Human Interface Guidelines、Auto Layout／Safe Area、Size Class、SF Symbols、String Catalog（ローカライズ） |
| Android | Material Design、ConstraintLayout／Compose レイアウト、画面密度・リソース修飾子、strings.xml、多言語・RTL |
| React Native | Flexbox、StyleSheet、SafeAreaView、Platform 別スタイル、i18n ライブラリ |

roadmap.sh の参照トピック：ios: hig, ui-design, auto-layout, simple-ui-building, building-interfaces / swift-ui: localization, font, padding, animations / android: interface--navigation, constraint, icon, text / react-native: layouts--flexbox, styling, stylesheets, css-basics, safeareaview, statusbar

## 評価を記録する

[個人のスキル評価書式](../../templates/individual-assessment.md)に、現在の判定、根拠、支援と制約、次の到達条件を記録します。
