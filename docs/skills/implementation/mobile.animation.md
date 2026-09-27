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

## このスキルについて

表示の切り替えや位置・大きさの変化に動きを付け、タップやスワイプなど指の操作に画面を反応させる技術です。モバイルアプリは指で直接画面を操作するため、動きが操作に遅れたりかくついたりすると使いにくさとして強く感じられ、限られた処理能力と電池の中で滑らかに描画する工夫が必要です。また、OS には動きを減らす設定があり、動きで気分が悪くなる利用者のためにその設定に従う対応も求められます。最初に押さえるのは、アニメーションは開始の状態と終了の状態の間を、時間とイージング（速度の変化の付け方）で補って見せる仕組みだということです。

分からない用語は[用語集](../../guide/glossary.md)で確認できます。

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

## 次のLvへ進むために

学習の目安として、次の段階に進むための課題と参考資料を示します。課題は評価の条件ではありません。

| 目標 | 取り組む課題の例 | 参考資料 |
| :--- | :--- | :--- |
| Lv1 | ボタンを押すと画像が表示・非表示になり、その際に透明度と位置が変わるアニメーションを公式の例に沿って付ける | [SwiftUI チュートリアル](https://developer.apple.com/tutorials/swiftui)・[Compose のアニメーション](https://developer.android.com/develop/ui/compose/animation/introduction)・[アニメーション（React Native）](https://reactnative.dev/docs/animations) |
| Lv2 | カードを左右にスワイプすると削除でき、途中で指を離すと元の位置に戻る一覧を作る。OS の動きを減らす設定をオンにしたときに動きを控えることを実機で確認する | [SwiftUI](https://developer.apple.com/documentation/swiftui)・[Compose のアニメーション](https://developer.android.com/develop/ui/compose/animation/introduction)・[アニメーション（React Native）](https://reactnative.dev/docs/animations)・[Accessibility](https://developer.apple.com/documentation/accessibility) |
| Lv3 | 動きがかくつく既存画面の描画時間を計測して原因を特定し、描画の負荷が少ない方法に置き換える。スワイプ中にアニメーションが中断されたときに画面の状態が食い違わないことを確認する | [Core Animation](https://developer.apple.com/documentation/quartzcore)・[アプリ性能の改善](https://developer.apple.com/documentation/xcode/improving-your-app-s-performance)・[View のアニメーション](https://developer.android.com/develop/ui/views/animations)・[パフォーマンス（Android）](https://developer.android.com/topic/performance)・[パフォーマンス（React Native）](https://reactnative.dev/docs/performance) |

## 技術の対応

| 用途 | iOS | Android | React Native |
| :--- | :--- | :--- | :--- |
| 状態の変化に連動する動き | SwiftUI の暗黙・明示アニメーション、Animatable | Compose の animate*AsState | Animated、Reanimated |
| 表示・非表示と切り替えの効果 | Transition | AnimatedVisibility、Transition | LayoutAnimation |
| 従来のUIと描画層のアニメーション | Core Animation、UIView.animate | MotionLayout、Property Animation | Animated、LayoutAnimation |
| ジェスチャ | ジェスチャ（UIGestureRecognizer、SwiftUI の Gesture） | pointerInput、GestureDetector | Gesture Handler |
| 滑らかさの確認 | Instruments（Core Animation） | Android Profiler、GPU レンダリング速度 | フレームレートの理解、Performance Monitor |

roadmap.sh で学ぶ：[iOS](https://roadmap.sh/ios)（Creating animations、Core Animation、View transitions）／[SwiftUI](https://roadmap.sh/swift-ui)（Animations、Implicit animations、Explicit animations、Animatable protocol、Transitions、Gestures）／[Android](https://roadmap.sh/android)（Animations）／[React Native](https://roadmap.sh/react-native)（Animations、Understand frame rates、Gesture handling）

## 評価を記録する

[個人のスキル評価書式](../../templates/individual-assessment.md)に、現在の判定、根拠、支援と制約、次の到達条件を記録します。
