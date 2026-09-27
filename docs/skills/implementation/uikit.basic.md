---
title: "UIKit"
description: "UIKitの基準と使い方。モバイルアプリ開発のスキル評価・チーム改善ガイド。"
---

# UIKit

**スキルID：** `uikit.basic`  
**スキル領域：** [フレームワーク・実装領域](index.md)  
**対象プラットフォーム：** iOS  
**主な前提：** Swift

[習熟度の共通定義と判定方法](../../guide/individual-assessment.md)に沿って、根拠を確認します。

## Lv0

ViewとView Controllerの役割、ライフサイクル、制約によるレイアウトを説明できず、単純な画面の変更にも手順ごとの指示が必要である。

## Lv1

例や支援に沿ってView Controllerを作成し、部品の配置、アウトレットとアクションの接続、画面の表示と遷移を実装できる。指定された端末サイズと操作で表示を確認できる。

## Lv2

要件が明確な画面をView ControllerとViewに分け、制約によるレイアウト、一覧表示、Delegateによるイベント処理、画面遷移を実装できる。ライフサイクル上の処理位置を選び、表示崩れや操作の不具合を自分で検証・修正できる。

## Lv3

肥大化したView Controller、制約の競合、セルの再利用、参照の保持に起因する不具合を分析できる。責務の分割や画面遷移の構成を設計し、他者の実装をレビューできる。

## Lv4

共通のView部品、画面構成と遷移の方針、レイアウト検証の基準を整備できる。他者の利用と既存画面の改修を支援し、表示不具合や改修工数の改善を確認できる。

## 技術の対応

| プラットフォーム | 主な技術・API |
| :--- | :--- |
| iOS | UIViewController とライフサイクル、UIView、Auto Layout（NSLayoutConstraint）、Storyboard／XIB、IBOutlet／IBAction、UINavigationController、Segue、モーダル表示、UITableView／UICollectionView、Delegate パターン |

roadmap.sh の参照トピック：ios: uikit, views-view-controllers, view-controllers, viewcontroller-lifecycle, views, components, storyboards, xibs, iboutlets, ibactions, navigation-controllers-segues, pushing-presenting, presenting--dismissing-views, modals-and-navigation, delegate-pattern, implementing-delegates, basic-interfaces, toolbar / swift-ui: uikit-vs-swiftui

## 評価を記録する

[個人のスキル評価書式](../../templates/individual-assessment.md)に、現在の判定、根拠、支援と制約、次の到達条件を記録します。
