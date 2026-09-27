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

## このスキルについて

SwiftUIは、iPhoneやiPadのアプリの画面を小さな部品（View）の組み合わせで作るAppleの仕組みで、画面サイズや文字サイズ、ダークモードなど端末ごとに異なる表示条件にも同じコードで対応します。宣言的UIと呼ばれる方式で、「この状態のときはこう表示する」と書いておけば、状態の値を書き換えるだけで画面が追従します。これに対してUIKitなどの命令的UIでは、ボタンやラベルといった部品を直接操作して表示を一つずつ書き換えるため、書き換え漏れによる表示の食い違いが起きやすくなります。最初に押さえるのは、画面は状態から作られるという考え方と、その状態をどのViewが持つか（状態の持ち主）を決めることです。

分からない用語は[用語集](../../guide/glossary.md)で確認できます。

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

## 次のLvへ進むために

学習の目安として、次の段階に進むための課題と参考資料を示します。課題は評価の条件ではありません。

| 目標 | 取り組む課題の例 | 参考資料 |
| :--- | :--- | :--- |
| Lv1 | SwiftUIチュートリアルに沿って、テキスト、画像、一覧を並べた画面を作り、ボタンを押すと数値が増えるカウンターを加えてプレビューで表示を確認する | [SwiftUIチュートリアル](https://developer.apple.com/tutorials/swiftui) |
| Lv2 | 一覧・詳細・追加フォームの3画面を持つToDoアプリを作り、NavigationStackで遷移し、@Bindingや@Observableで状態を受け渡す。起動時にサンプルデータを非同期で読み込み、読み込み中の表示も付ける | [SwiftUI](https://developer.apple.com/documentation/swiftui)・[Swift Concurrency](https://developer.apple.com/documentation/swift/concurrency) |
| Lv3 | 既存の画面で入力中の値が消える、一覧全体が描き直されるといった問題を再現し、状態の初期化位置や監視範囲を見直して改善する。UIViewRepresentableでUIKitの部品を1つ組み込み、両者の境界での責務を文書にまとめる | [SwiftUI](https://developer.apple.com/documentation/swiftui)・[アプリ性能の改善](https://developer.apple.com/documentation/xcode/improving-your-app-s-performance) |

## 技術の対応

| 用途 | 主な技術・API |
| :--- | :--- |
| 画面の部品 | ViewとViewModifier、@ViewBuilder |
| 配置と一覧 | VStack／HStack／ZStack、List、Form、Grid、GeometryReader |
| 状態の管理 | @State／@Binding／@StateObject／@ObservedObject／@EnvironmentObject／@Observable |
| 画面遷移 | NavigationStack／NavigationPath／TabView |
| 操作とデータ表示 | ジェスチャ、Drag & Drop、Swift Charts |
| UIKitとの相互運用 | UIViewRepresentable |

roadmap.shで学ぶ：[iOS](https://roadmap.sh/ios)（SwiftUI、Declarative syntax、Views and modifiers、State management、Navigation stacks）／[SwiftUI](https://roadmap.sh/swift-ui)（ViewBuilder、State、Binding、Data flow、NavigationStack、Gestures、UIKit vs SwiftUI）

## 評価を記録する

[個人のスキル評価書式](../../templates/individual-assessment.md)に、現在の判定、根拠、支援と制約、次の到達条件を記録します。
