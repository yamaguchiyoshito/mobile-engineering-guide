---
title: "入力とバリデーション"
description: "入力とバリデーションの基準と使い方。モバイルアプリ開発のスキル評価・チーム改善ガイド。"
---

# 入力とバリデーション

**スキルID：** `mobile.input-validation`  
**スキル領域：** [フレームワーク・実装領域](index.md)  
**対象プラットフォーム：** 共通  
**主な前提：** UI実装

[習熟度の共通定義と判定方法](../../guide/individual-assessment.md)に沿って、根拠を確認します。

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

## 技術の対応

| プラットフォーム | 主な技術・API |
| :--- | :--- |
| iOS | UITextField／TextField、キーボード種別、キーボード回避、フォーカス管理、入力検証とエラー表示、Formatter |
| Android | TextField／EditText、InputType、IME アクション、入力検証、エラー表示 |
| React Native | TextInput、KeyboardAvoidingView、フォームライブラリ（React Hook Form） |

roadmap.sh の参照トピック：ios: user-interactions, ibactions, iboutlets / android: textfield, textview / react-native: text-input, keyboardavoidingview, gesture-handling, interactions / swift-ui: user-interaction, ui-controls, form

## 評価を記録する

[個人のスキル評価書式](../../templates/individual-assessment.md)に、現在の判定、根拠、支援と制約、次の到達条件を記録します。
