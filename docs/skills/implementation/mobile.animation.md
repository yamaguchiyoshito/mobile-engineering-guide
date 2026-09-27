---
title: "アニメーションとインタラクション"
description: "アニメーションとインタラクションの基準と使い方。モバイルアプリ開発のスキル評価・チーム改善ガイド。"
---

# アニメーションとインタラクション

**スキルID：** `mobile.animation`  
**スキル領域：** [フレームワーク・実装領域](index.md)  
**対象プラットフォーム：** 共通  
**主な前提：** UI実装

[習熟度の共通定義と判定方法](../../guide/individual-assessment.md)に沿って、根拠を確認します。

## Lv0

アニメーションの開始・終了状態、時間、イージングと画面状態の関係を説明できず、動きの追加に手順ごとの指示が必要である。

## Lv1

例に沿って表示・非表示や位置・透明度の変化に単純なアニメーションを付けられる。指定された操作で動きを確認できる。

## Lv2

状態変化に連動するアニメーション、画面遷移の効果、タップやスワイプなどのジェスチャを要件どおりに実装できる。OSの動きを減らす設定に対応し、実機で動きと操作を検証・修正できる。

## Lv3

フレーム落ち、ジェスチャとアニメーションの競合、中断時の状態の不整合を分析し、描画への負荷を抑えた実装方法を選べる。複数の要素が連動するアニメーションを設計し、他者の実装をレビューできる。

## Lv4

動きの時間やイージングの基準、共通アニメーション部品、フレームレートの検証方法を整備できる。他者の利用を支援し、動きのばらつきや性能問題の減少を確認できる。

## 技術の対応

| プラットフォーム | 主な技術・API |
| :--- | :--- |
| iOS | SwiftUI の暗黙・明示アニメーション、Animatable、Transition、Core Animation、UIView.animate、ジェスチャ |
| Android | Compose の animate*AsState、AnimatedVisibility、Transition、MotionLayout、Property Animation |
| React Native | Animated、Reanimated、Gesture Handler、LayoutAnimation、フレームレートの理解 |

roadmap.sh の参照トピック：ios: basics--creating-animations, core-animation, view-transitions / android: animations / react-native: animations, understand-frame-rates, gesture-handling, interactions / swift-ui: animations, implicit-animations, explicit-animations, animatable-protocol, transitions, gestures, clipshape

## 評価を記録する

[個人のスキル評価書式](../../templates/individual-assessment.md)に、現在の判定、根拠、支援と制約、次の到達条件を記録します。
