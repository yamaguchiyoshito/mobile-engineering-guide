---
title: "アプリアーキテクチャと依存性注入"
description: "アプリアーキテクチャと依存性注入の基準と使い方。モバイルアプリ開発の習熟度評価・チーム改善ガイド。"
---

# アプリアーキテクチャと依存性注入

**要素技術ID：** `mobile.architecture`  
**技術領域：** [フレームワーク・実装領域](index.md)  
**対象プラットフォーム：** 共通  
**主な前提：** UI実装、リアクティブプログラミング

[習熟度の共通定義と判定方法](../../guide/individual-assessment.md)に沿って、根拠を確認します。

## この要素技術について

アプリのコードを、画面の表示、画面の状態、データの取得や保存といった役割ごとに分け、部品同士のつながり方を決める技術です。1つの画面のコードに表示と通信と保存をすべて書くと、小さな変更が思わぬ箇所を壊したり、通信せずに動作を確かめるテストが書けなくなったりします。モバイルアプリでは、画面の回転やアプリの中断で表示が作り直されても状態を保ち、通信が途切れても保存済みのデータで動き続ける必要があるため、表示と状態とデータを分けておくことが特に重要です。MVVMなどのパターン名は、この分け方の型に付けられた名前です。最初に押さえるのは3つの役割の分け方と、部品が使う相手を内部で作らずに外から渡す依存性注入の考え方です。

分からない用語は[用語集](../../guide/glossary.md)で確認できます。

## Lv0

画面、状態、データ取得の責務の違いや依存関係の向きを説明できず、既存構成への機能追加にも手順ごとの指示が必要である。

## Lv1

既存のアーキテクチャに沿って、指定された層に画面や処理を追加できる。依存の注入やテスト用の差し替えは例に従って実装できる。

## Lv2

要件が明確な機能を表示層、状態を持つ層、データ層に分け、依存性注入で結合を切り離して実装できる。層ごとの責務を守ってユニットテストを書き、通常の機能追加と修正を完了できる。

## Lv3

画面の規模、チームの人数、テストのしやすさ、ビルド時間などの制約から、アーキテクチャパターンやモジュール分割を比較・選択できる。層の越境や循環依存を分析し、既存構成を段階的に改善して他者の設計をレビューできる。

## Lv4

アーキテクチャの方針、ひな形、依存ルールの自動検査を整備し、チームで再現できる構成にできる。他者の利用と移行を支援し、変更の影響範囲や実装工数の改善を確認して方針を更新できる。

## 次のLvへ進むために

学習の目安として、次の段階に進むための課題と参考資料を示します。課題は評価の条件ではありません。

| 目標 | 取り組む課題の例 | 参考資料 |
| :--- | :--- | :--- |
| Lv1 | 公式のアーキテクチャガイドやチームの既存アプリを読み、画面・状態・データの各役割がどのファイルにあるかを図に書き出す。そのうえで、指定された層に表示項目を1つ追加する | [アプリアーキテクチャガイド](https://developer.android.com/topic/architecture) |
| Lv2 | 一覧と詳細の2画面を持つアプリを、表示・状態・データ取得の3層に分けて作る。データ取得の部品を外から渡せるようにし、偽のデータを渡して状態の層のユニットテストを書く | [アプリアーキテクチャガイド](https://developer.android.com/topic/architecture)・[依存性注入](https://developer.android.com/training/dependency-injection)・[XCTest](https://developer.apple.com/documentation/xctest)・[テストの概要（React Native）](https://reactnative.dev/docs/testing-overview) |
| Lv3 | 既存アプリの依存関係を図にして、層の越境や循環依存を見つけ、1か所を段階的に直す。画面数やチームの人数を想定して2つ以上のパターンを比較し、選択の理由を文書にまとめる | [アプリアーキテクチャガイド](https://developer.android.com/topic/architecture)・[Swift Package Manager](https://developer.apple.com/documentation/xcode/swift-packages) |

## 技術の対応

| 用途 | iOS | Android | React Native |
| :--- | :--- | :--- | :--- |
| 画面と状態の分け方 | MVC、MVVM、MVVM-C、VIPER、TCA | MVVM、MVI | コンテナ・プレゼンテーション分離、状態管理ライブラリ（Redux、Zustand） |
| データ層・処理層の分け方 | Clean Architecture | Repositoryパターン、UseCase | サービス層とフックの分離、Repository |
| 依存性注入 | SwiftのDI（イニシャライザ注入、Environment、Factory） | Hilt／Dagger、Koin、Kodein | Contextによる注入 |
| モジュール分割 | モジュール分割（SPM） | マルチモジュール | 機能ディレクトリ単位の分割、モノレポのパッケージ |

## 関連ライブラリと参考資料

主な一次情報の所在です。掲載は公式資料と、技術の対応表に挙げた広く使われるライブラリに限ります。採用を推奨するものではありません。

<!-- references:start ids="android-architecture, android-ui-layer, android-data-layer, android-domain-layer, android-dependency-injection, android-hilt, dagger, koin, kodein, android-modularization, swiftui-environment, swift-packages, swift-composable-architecture, redux, zustand" -->

| 種別 | 名称 | 対象 | 概要 |
| :--- | :--- | :--- | :--- |
| 公式リファレンス | [Environment](https://developer.apple.com/documentation/swiftui/environment) | iOS | View階層を通じて値や依存を受け渡すためのプロパティラッパー |
| 公式リファレンス | [Swift packages](https://developer.apple.com/documentation/xcode/swift-packages) | iOS | Swift Package Managerでコードを分割・共有する方法 |
| 公式リファレンス | [Hilt](https://developer.android.com/training/dependency-injection/hilt-android) | Android | Daggerを基にAndroid向けに依存性注入を行うJetpackライブラリ |
| ライブラリ | [The Composable Architecture](https://github.com/pointfreeco/swift-composable-architecture) | iOS | 状態・アクション・副作用を一方向の流れで管理するSwiftライブラリ |
| ライブラリ | [Dagger](https://dagger.dev/) | Android | コンパイル時に依存関係のコードを生成する依存性注入ライブラリ |
| ライブラリ | [Koin](https://insert-koin.io/) | Android | Kotlinの記述で依存関係を定義して注入するライブラリ |
| ライブラリ | [Kodein](https://kosi-libs.org/kodein/) | Android | Kotlin向けに依存関係の定義と注入を行うライブラリ |
| ライブラリ | [Redux](https://github.com/reduxjs/redux) | React Native | アプリ全体の状態を1つのストアで管理するJavaScriptライブラリ |
| ライブラリ | [Zustand](https://github.com/pmndrs/zustand) | React Native | フックでストアの状態を読み書きする状態管理ライブラリ |
| 学習資料 | [アプリアーキテクチャガイド（Android）](https://developer.android.com/topic/architecture) | Android | UI層・データ層などに分けてアプリを構成するための公式ガイド |
| 学習資料 | [UI layer](https://developer.android.com/topic/architecture/ui-layer) | Android | UIの状態とイベントを単方向の流れで扱うUI層の設計指針 |
| 学習資料 | [Data layer](https://developer.android.com/topic/architecture/data-layer) | Android | Repositoryでデータの取得元をまとめるデータ層の設計指針 |
| 学習資料 | [Domain layer](https://developer.android.com/topic/architecture/domain-layer) | Android | UseCaseで業務ロジックを切り出すドメイン層の設計指針 |
| 学習資料 | [依存性注入（Android）](https://developer.android.com/training/dependency-injection) | Android | Androidアプリで依存性注入を使う考え方と手順 |
| 学習資料 | [Guide to Android app modularization](https://developer.android.com/topic/modularization) | Android | アプリを複数のGradleモジュールに分ける方法の解説 |

<!-- references:end -->

## 評価を記録する

[個人の習熟度評価書式](../../templates/individual-assessment.md)に、現在の判定、根拠、支援と制約、次の到達条件を記録します。
