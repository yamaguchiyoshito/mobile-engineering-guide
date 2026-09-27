---
title: "Jetpack Compose"
description: "Jetpack Composeの基準と使い方。モバイルアプリ開発のスキル評価・チーム改善ガイド。"
---

# Jetpack Compose

**スキルID：** `compose.basic`  
**スキル領域：** [フレームワーク・実装領域](index.md)  
**対象プラットフォーム：** Android  
**主な前提：** Kotlin、Kotlinコルーチン

[習熟度の共通定義と判定方法](../../guide/individual-assessment.md)に沿って、根拠を確認します。

## Lv0

Composable、状態、再コンポジションの関係を説明できず、単純な画面の変更にも手順ごとの指示が必要である。

## Lv1

例や支援に沿ってComposableを作成・変更し、行・列による配置、一覧、単純な状態の保持と更新を実装できる。指定された操作とプレビューで表示を確認できる。

## Lv2

要件が明確な画面をComposableに分け、状態ホイスティングで状態と表示を分離できる。ViewModelの状態の購読、副作用、画面遷移を含む通常の画面を実装し、表示と操作を自分で検証・修正できる。

## Lv3

不要な再コンポジション、副作用の起動条件、構成変更やプロセス終了時の状態消失を分析できる。複雑な画面の状態配置と部品構成を設計し、既存のView実装との共存を含めて他者の実装をレビューできる。

## Lv4

共通Composable、テーマ、状態の受け渡し方針、プレビューとUI検証の基準を整備できる。他者の利用と移行を支援し、同種不具合や画面実装工数の改善を確認できる。

## 技術の対応

| プラットフォーム | 主な技術・API |
| :--- | :--- |
| Android | Composable 関数、remember／rememberSaveable、State ホイスティング、再コンポジション、副作用（LaunchedEffect、DisposableEffect）、Column／Row／Box、LazyColumn／LazyRow、Scaffold、TabRow、Navigation Compose（NavHost）、ViewModel との接続、Material 3 |

roadmap.sh の参照トピック：android: jetpack-compose, remember--state, state-changes, side-effects, column--row, box, lazy-column--row, scaffold, tabrow, navhost, viewmodel-state, button, text, textfield, card, image

## 評価を記録する

[個人のスキル評価書式](../../templates/individual-assessment.md)に、現在の判定、根拠、支援と制約、次の到達条件を記録します。
