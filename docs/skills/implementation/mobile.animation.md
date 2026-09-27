---
title: "アニメーションとインタラクション"
description: "アニメーションとインタラクションの基準と使い方。モバイルアプリ開発の習熟度評価・チーム改善ガイド。"
---

# アニメーションとインタラクション

**要素技術ID：** `mobile.animation`  
**技術領域：** [フレームワーク・実装領域](index.md)  
**対象プラットフォーム：** 共通  
**主な前提：** UI実装

[習熟度の共通定義と判定方法](../../guide/individual-assessment.md)に沿って、根拠を確認します。

## この要素技術について

表示の切り替えや位置・大きさの変化に動きを付け、タップやスワイプなど指の操作に画面を反応させる技術です。モバイルアプリは指で直接画面を操作するため、動きが操作に遅れたりかくついたりすると使いにくさとして強く感じられ、限られた処理能力と電池の中で滑らかに描画する工夫が必要です。また、OSには動きを減らす設定があり、動きで気分が悪くなる利用者のためにその設定に従う対応も求められます。最初に押さえるのは、アニメーションは開始の状態と終了の状態の間を、時間とイージング（速度の変化の付け方）で補って見せる仕組みだということです。

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
| Lv1 | ボタンを押すと画像が表示・非表示になり、その際に透明度と位置が変わるアニメーションを公式の例に沿って付ける | [SwiftUIチュートリアル](https://developer.apple.com/tutorials/swiftui)・[Composeのアニメーション](https://developer.android.com/develop/ui/compose/animation/introduction)・[アニメーション（React Native）](https://reactnative.dev/docs/animations) |
| Lv2 | カードを左右にスワイプすると削除でき、途中で指を離すと元の位置に戻る一覧を作る。OSの動きを減らす設定をオンにしたときに動きを控えることを実機で確認する | [SwiftUI](https://developer.apple.com/documentation/swiftui)・[Composeのアニメーション](https://developer.android.com/develop/ui/compose/animation/introduction)・[アニメーション（React Native）](https://reactnative.dev/docs/animations)・[Accessibility](https://developer.apple.com/documentation/accessibility) |
| Lv3 | 動きがかくつく既存画面の描画時間を計測して原因を特定し、描画の負荷が少ない方法に置き換える。スワイプ中にアニメーションが中断されたときに画面の状態が食い違わないことを確認する | [Core Animation](https://developer.apple.com/documentation/quartzcore)・[アプリ性能の改善](https://developer.apple.com/documentation/xcode/improving-your-app-s-performance)・[Viewのアニメーション](https://developer.android.com/develop/ui/views/animations)・[パフォーマンス（Android）](https://developer.android.com/topic/performance)・[パフォーマンス（React Native）](https://reactnative.dev/docs/performance) |

## 技術の対応

| 用途 | iOS | Android | React Native |
| :--- | :--- | :--- | :--- |
| 状態の変化に連動する動き | SwiftUIの暗黙・明示アニメーション、Animatable | Composeのanimate*AsState | Animated、Reanimated |
| 表示・非表示と切り替えの効果 | Transition | AnimatedVisibility、Transition | LayoutAnimation |
| 従来のUIと描画層のアニメーション | Core Animation、UIView.animate | MotionLayout、Property Animation | Animated、LayoutAnimation |
| ジェスチャ | ジェスチャ（UIGestureRecognizer、SwiftUIのGesture） | pointerInput、GestureDetector | Gesture Handler |
| 滑らかさの確認 | Instruments（Core Animation） | Android Profiler、GPUレンダリング速度 | フレームレートの理解、Performance Monitor |

## 関連ライブラリと参考資料

主な一次情報の所在です。掲載は公式資料と、技術の対応表に挙げた広く使われるライブラリに限ります。採用を推奨するものではありません。

<!-- references:start ids="swiftui-animations, core-animation, uikit-uiview-animate, uikit-uigesturerecognizer, swiftui-gestures, compose-animation, android-motionlayout, android-property-animation, compose-gestures, android-gpu-rendering, rn-animated, rn-layoutanimation, react-native-reanimated, react-native-gesture-handler, rn-performance" -->

| 種別 | 名称 | 対象 | 概要 |
| :--- | :--- | :--- | :--- |
| 公式リファレンス | [Animations](https://developer.apple.com/documentation/swiftui/animations) | iOS | 状態の変化に合わせてViewの変化を動かすAPI群 |
| 公式リファレンス | [Core Animation](https://developer.apple.com/documentation/quartzcore) | iOS | 描画層のレイヤーを使って表示と動きを処理するフレームワーク |
| 公式リファレンス | [UIView.animate(withDuration:animations:)](https://developer.apple.com/documentation/uikit/uiview/animate(withduration:animations:)) | iOS | Viewのプロパティ変化を指定時間で動かすメソッド |
| 公式リファレンス | [UIGestureRecognizer](https://developer.apple.com/documentation/uikit/uigesturerecognizer) | iOS | タップやスワイプなどの操作を認識する基底クラス |
| 公式リファレンス | [Gestures](https://developer.apple.com/documentation/swiftui/gestures) | iOS | タップやドラッグなどの操作を認識してViewに結び付けるAPI群 |
| 公式リファレンス | [Composeのアニメーション（Android）](https://developer.android.com/develop/ui/compose/animation/introduction) | Android | animate*AsStateなどComposeのアニメーションAPIの解説 |
| 公式リファレンス | [MotionLayout](https://developer.android.com/develop/ui/views/animations/motionlayout) | Android | レイアウト間の遷移と動きを宣言的に定義するレイアウト |
| 公式リファレンス | [Property Animation Overview](https://developer.android.com/develop/ui/views/animations/prop-animation) | Android | オブジェクトのプロパティ値を時間に沿って変化させる仕組み |
| 公式リファレンス | [Understand gestures](https://developer.android.com/develop/ui/compose/touch-input/pointer-input/understand-gestures) | Android | pointerInputやジェスチャ検出でタッチ操作を扱う方法 |
| 公式リファレンス | [Inspect rendering speed](https://developer.android.com/topic/performance/rendering/inspect-gpu-rendering) | Android | GPUレンダリング速度とオーバードローを確認する方法 |
| 公式リファレンス | [Animated](https://reactnative.dev/docs/animated) | React Native | 値の変化を時間に沿って補間して部品を動かすAPI |
| 公式リファレンス | [LayoutAnimation](https://reactnative.dev/docs/layoutanimation) | React Native | 次のレイアウト更新時に位置や大きさの変化を動かすAPI |
| ライブラリ | [React Native Reanimated](https://github.com/software-mansion/react-native-reanimated) | React Native | UIスレッドでアニメーションを実行するReact Native向けライブラリ |
| ライブラリ | [React Native Gesture Handler](https://github.com/software-mansion/react-native-gesture-handler) | React Native | ネイティブ側でタッチ操作を認識するReact Native向けライブラリ |
| 学習資料 | [パフォーマンス（React Native）](https://reactnative.dev/docs/performance) | React Native | フレームレートの考え方と表示が遅くなる原因の解説 |

<!-- references:end -->

## 評価を記録する

[個人の習熟度評価書式](../../templates/individual-assessment.md)に、現在の判定、根拠、支援と制約、次の到達条件を記録します。
