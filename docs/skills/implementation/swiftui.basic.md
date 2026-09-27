---
title: "SwiftUI"
description: "SwiftUIの基準と使い方。モバイルアプリ開発のスキル評価・チーム改善ガイド。"
---

# SwiftUI

**スキルID：** `swiftui.basic`  
**スキル領域：** [フレームワーク・実装領域](index.md)  
**対象プラットフォーム：** iOS  
**主な前提：** Swift、Swift並行処理

[習熟度の共通定義と判定方法](../../guide/individual-assessment.md)に沿って、根拠を確認します。

## Lv0

View、modifier、状態と表示の関係を説明できず、単純な画面の変更にも手順ごとの指示が必要である。

## Lv1

例や支援に沿ってViewを組み合わせ、スタックによる配置、一覧、単純な状態の更新を実装できる。指定された操作とプレビューで表示を確認できる。

## Lv2

要件が明確な画面をViewに分け、状態の持ち主を決めてバインディングや監視対象オブジェクトで受け渡せる。画面遷移、フォーム、非同期の読み込みを含む通常の画面を実装し、表示と操作を自分で検証・修正できる。

## Lv3

Viewの再生成、状態の初期化位置、監視範囲の広さに起因する不要な再描画や状態の消失を分析できる。複雑な画面の構造、状態の配置、命令的UIとの相互運用の境界を設計し、他者の実装をレビューできる。

## Lv4

View部品、状態の受け渡し方針、プレビューとUI検証の基準を整備できる。他者の利用と更新対応を支援し、同種不具合や画面実装工数の改善を確認できる。

## 技術の対応

| プラットフォーム | 主な技術・API |
| :--- | :--- |
| iOS | View と ViewModifier、@ViewBuilder、VStack／HStack／ZStack、List、Form、Grid、GeometryReader、@State／@Binding／@StateObject／@ObservedObject／@EnvironmentObject／@Observable、NavigationStack／NavigationPath／TabView、ジェスチャ、Drag & Drop、Swift Charts、UIKit との相互運用（UIViewRepresentable） |

roadmap.sh の参照トピック：ios: swiftui, declarative-syntax, views-and-modifiers, state-management, navigation-view, navigationlink, navigation-stacks / swift-ui: what-is-swiftui, views, viewbuilder, vstack, hstack, zstack, list, form, grid, geometryreader, state, binding, stateobject, observedobject, environmentobject, data-flow, navigationstack, navigationpath, navigationlink, tabview, gestures, drag--drop, swift-charts, uikit-vs-swiftui, swiftui-inspector

## 評価を記録する

[個人のスキル評価書式](../../templates/individual-assessment.md)に、現在の判定、根拠、支援と制約、次の到達条件を記録します。
