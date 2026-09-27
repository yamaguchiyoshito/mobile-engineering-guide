---
title: "UIKit"
description: "UIKitの基準と使い方。モバイルアプリ開発の習熟度評価・チーム改善ガイド。"
---

# UIKit

**要素技術ID：** `uikit.basic`  
**技術領域：** [フレームワーク・実装領域](index.md)  
**対象プラットフォーム：** iOS  
**主な前提：** Swift

[習熟度の共通定義と判定方法](../../guide/individual-assessment.md)に沿って、根拠を確認します。

## この要素技術について

UIKitは、iPhoneやiPadのアプリの画面を、画面単位の管理役（View Controller）と、その上に置く部品（View）で組み立てるAppleの仕組みです。命令的UIと呼ばれる方式で、ボタンやラベルなどの部品を直接取り出して表示や位置を書き換えます。SwiftUIより前から使われており、既存のアプリの多くがUIKitで作られているため、保守やSwiftUIとの併用で読み書きする場面が多くあります。最初に押さえるのは、View Controllerが表示されてから消えるまでに呼ばれる処理の順序（ライフサイクル）と、部品同士の位置関係を制約（Auto Layout）で指定して画面サイズの異なる端末に対応する考え方です。

分からない用語は[用語集](../../guide/glossary.md)で確認できます。

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

## 次のLvへ進むために

学習の目安として、次の段階に進むための課題と参考資料を示します。課題は評価の条件ではありません。

| 目標 | 取り組む課題の例 | 参考資料 |
| :--- | :--- | :--- |
| Lv1 | Storyboardで1画面を作り、ボタンとラベルをIBOutlet／IBActionで接続して、タップで表示が変わることを画面サイズの異なる2種類のシミュレーターで確認する | [UIKit](https://developer.apple.com/documentation/uikit)・[Xcode](https://developer.apple.com/documentation/xcode) |
| Lv2 | UITableViewの一覧と詳細の2画面を持つメモアプリをUINavigationControllerで作り、一覧の選択をDelegateで受け取る。Auto Layoutで配置し、端末を横向きにしても表示が崩れないことを確認する | [UIKit](https://developer.apple.com/documentation/uikit)・[Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines) |
| Lv3 | 肥大化したView Controllerを1つ選び、表示・データ取得・画面遷移の処理を別の型に分ける。セルの再利用による表示の混在や、クロージャが参照を保持し続けることによるメモリリークをXcodeで確認して解消する | [UIKit](https://developer.apple.com/documentation/uikit)・[アプリ性能の改善](https://developer.apple.com/documentation/xcode/improving-your-app-s-performance) |

## 技術の対応

| 用途 | 主な技術・API |
| :--- | :--- |
| 画面の管理 | UIViewControllerとライフサイクル、UIView |
| レイアウト | Auto Layout（NSLayoutConstraint）、Storyboard／XIB |
| 部品とイベントの接続 | IBOutlet／IBAction、Delegateパターン |
| 画面遷移 | UINavigationController、Segue、モーダル表示 |
| 一覧表示 | UITableView／UICollectionView |

## 関連ライブラリと参考資料

主な一次情報の所在です。掲載は公式資料と、技術の対応表に挙げた広く使われるライブラリに限ります。採用を推奨するものではありません。

<!-- references:start ids="uikit, uikit-uiviewcontroller, uikit-uiview, nslayoutconstraint, uikit-uistoryboard, uikit-uinavigationcontroller, uikit-uistoryboardsegue, uikit-present, uikit-uitableview, uikit-uicollectionview, xcode, hig" -->

| 種別 | 名称 | 対象 | 概要 |
| :--- | :--- | :--- | :--- |
| 公式リファレンス | [UIKit](https://developer.apple.com/documentation/uikit) | iOS | ViewとView Controllerで画面を構築するUIフレームワーク |
| 公式リファレンス | [UIViewController](https://developer.apple.com/documentation/uikit/uiviewcontroller) | iOS | 画面のViewとライフサイクルを管理する基底クラス |
| 公式リファレンス | [UIView](https://developer.apple.com/documentation/uikit/uiview) | iOS | 画面上の矩形領域の描画と操作を扱う基底クラス |
| 公式リファレンス | [NSLayoutConstraint](https://developer.apple.com/documentation/uikit/nslayoutconstraint) | iOS | Auto Layoutでビュー同士の位置と大きさの関係を定義する制約 |
| 公式リファレンス | [UIStoryboard](https://developer.apple.com/documentation/uikit/uistoryboard) | iOS | Storyboardに定義した画面を読み込むためのクラス |
| 公式リファレンス | [UINavigationController](https://developer.apple.com/documentation/uikit/uinavigationcontroller) | iOS | 画面を積み重ねて階層的な遷移を管理するコンテナ |
| 公式リファレンス | [UIStoryboardSegue](https://developer.apple.com/documentation/uikit/uistoryboardsegue) | iOS | Storyboard上の2つの画面間の遷移を表すクラス |
| 公式リファレンス | [present(_:animated:completion:)](https://developer.apple.com/documentation/uikit/uiviewcontroller/present(_:animated:completion:)) | iOS | View Controllerをモーダルで表示するメソッド |
| 公式リファレンス | [UITableView](https://developer.apple.com/documentation/uikit/uitableview) | iOS | 1列に並んだ行で項目の一覧を表示するView |
| 公式リファレンス | [UICollectionView](https://developer.apple.com/documentation/uikit/uicollectionview) | iOS | 指定したレイアウトで項目の集まりを表示するView |
| 公式リファレンス | [Xcode](https://developer.apple.com/documentation/xcode) | iOS | Appleプラットフォーム向けアプリを開発する環境のドキュメント |
| 公式リファレンス | [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines) | iOS | Appleのプラットフォームで画面や操作を設計するための指針 |

<!-- references:end -->

roadmap.shで学ぶ：[iOS](https://roadmap.sh/ios)（UIKit、View controllers、ViewController lifecycle、Storyboards、Xibs、Navigation controllers & segues、Delegate pattern）／[SwiftUI](https://roadmap.sh/swift-ui)（UIKit vs SwiftUI）

## 評価を記録する

[個人の習熟度評価書式](../../templates/individual-assessment.md)に、現在の判定、根拠、支援と制約、次の到達条件を記録します。
