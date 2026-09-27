---
title: "UIテスト・E2E"
description: "UIテスト・E2Eの基準と使い方。モバイルアプリ開発の習熟度評価・チーム改善ガイド。"
---

# UIテスト・E2E

**要素技術ID：** `test.ui`  
**技術領域：** [品質・高度化領域](index.md)  
**対象プラットフォーム：** 共通  
**主な前提：** UI実装、テスト設計

[習熟度の共通定義と判定方法](../../guide/individual-assessment.md)に沿って、根拠を確認します。

## この要素技術について

ボタンを押す、文字を入力するといった利用者の操作をプログラムで再現し、画面の表示や一連の流れが期待どおりかを自動で確かめる技術です。E2E（エンドツーエンド）テストは、アプリの起動から目的の操作の完了までを通して確かめるテストを指します。モバイルアプリのテストはシミュレータ・エミュレータや実機の上で動かす必要があり、権限の確認ダイアログ、アプリの中断と復帰、通信状態の変化など端末特有の出来事も起こるため、結果が不安定になりやすい特徴があります。最初に押さえるのは、画面上の要素を識別子で特定することと、表示が終わるまで適切に待ってから検証することです。

分からない用語は[用語集](../../guide/glossary.md)で確認できます。

## Lv0

利用者の操作シナリオとUIテスト・E2Eの検証範囲を説明できず、シミュレータ・エミュレータの準備や既存テストの実行に支援が必要である。

## Lv1

用意された手順とテストデータを使って画面操作を自動化し、指定された表示と完了結果を確認できる。失敗の調査は支援を受けて行える。

## Lv2

主要な利用シナリオについて、開始状態、操作、期待結果、後始末を実装できる。識別子による安定した要素の特定と待機方法を選び、CIで実行して失敗時の画面記録やログを確認できる。

## Lv3

権限ダイアログ、ディープリンク、バックグラウンドからの復帰、通信状態の変化、複数の画面サイズを含むシナリオを設計できる。アプリ、テスト、データ、端末環境の問題を切り分け、並列実行、データ分離、不安定なテストの隔離で安定性と速度を改善できる。

## Lv4

リスクに基づく自動化対象と実行端末の選定、共通の操作部品、データ・環境管理、結果分析と保守の体制を整備できる。チームで運用し、実行時間、不安定な失敗、重大不具合の検出状況が改善したことを確認できる。

## 次のLvへ進むために

学習の目安として、次の段階に進むための課題と参考資料を示します。課題は評価の条件ではありません。

| 目標 | 取り組む課題の例 | 参考資料 |
| :--- | :--- | :--- |
| Lv1 | 公式ドキュメントの手順に沿って、ログイン画面でIDとパスワードを入力してボタンを押し、次の画面の見出しが表示されることを確かめるUIテストを1件作り、シミュレータ・エミュレータで実行する | [XCTest](https://developer.apple.com/documentation/xctest)・[テスト（Android）](https://developer.android.com/training/testing)・[テストの概要（React Native）](https://reactnative.dev/docs/testing-overview) |
| Lv2 | 一覧・詳細・編集の3画面を持つメモアプリで、「メモを作成すると一覧に表示される」「編集内容が詳細画面に反映される」などの主要シナリオを識別子と待機を使って自動化する。テストごとにデータを初期化し、CIで実行して失敗時の画面記録とログを確認する | [XCTest](https://developer.apple.com/documentation/xctest)・[テスト（Android）](https://developer.android.com/training/testing)・[テストの概要（React Native）](https://reactnative.dev/docs/testing-overview)・[GitHub Actions](https://docs.github.com/ja/actions) |
| Lv3 | 既存アプリのUIテストに、権限ダイアログ、ディープリンクからの起動、通信の切断、バックグラウンドからの復帰を含むシナリオを追加する。複数の端末・画面サイズで並列実行し、不安定なテストの原因をアプリ・テスト・データ・端末環境に分類して改善する | [Firebase Test Lab](https://firebase.google.com/docs/test-lab)・[テスト（Android）](https://developer.android.com/training/testing)・[XCTest](https://developer.apple.com/documentation/xctest) |

## 技術の対応

| 用途 | iOS | Android | React Native |
| :--- | :--- | :--- | :--- |
| 画面操作の自動化 | XCUITest | Espresso、Compose UI Test、UI Automator | Detox、Appium、Maestro |
| 画面要素の特定 | Accessibility Identifier | testTag、contentDescription | testID |
| 表示結果の比較 | スナップショットテスト | Composeのスクリーンショットテスト | Jestのスナップショット |
| 端末上での実行環境 | SimulatorでのCI実行 | Firebase Test Lab | Detox（Simulator／Emulator） |

## 関連ライブラリと参考資料

主な一次情報の所在です。掲載は公式資料と、技術の対応表に挙げた広く使われるライブラリに限ります。採用を推奨するものではありません。

<!-- references:start ids="xcuiautomation, uikit-accessibility-identifier, swiftui-accessibility-identifier, xcode-running-tests, espresso, compose-testing, compose-testing-semantics, ui-automator, compose-screenshot-testing, firebase-test-lab, detox, appium, maestro, rn-view-testid, jest" -->

| 種別 | 名称 | 対象 | 概要 |
| :--- | :--- | :--- | :--- |
| 公式リファレンス | [XCUIAutomation](https://developer.apple.com/documentation/xcuiautomation) | iOS | 画面操作を再現してUIが意図どおり動くことを確認するUIテストのAPI |
| 公式リファレンス | [accessibilityIdentifier（UIKit）](https://developer.apple.com/documentation/uikit/uiaccessibilityidentification/accessibilityidentifier) | iOS | UIテストで画面要素を特定するための識別子を設定するプロパティ |
| 公式リファレンス | [accessibilityIdentifier(_:)（SwiftUI）](https://developer.apple.com/documentation/swiftui/view/accessibilityidentifier(_:)) | iOS | SwiftUIのビューにUIテスト用の識別子を付けるモディファイア |
| 公式リファレンス | [テストの実行と結果の確認（iOS）](https://developer.apple.com/documentation/xcode/running-tests-and-interpreting-results) | iOS | Xcodeやコマンドラインでテストを実行し、結果を読み取る方法 |
| 公式リファレンス | [Espresso](https://developer.android.com/training/testing/espresso) | Android | View階層を操作して画面の表示と動作を検証するUIテストのAPI |
| 公式リファレンス | [Composeのテスト（Android）](https://developer.android.com/develop/ui/compose/testing) | Android | Jetpack ComposeのUIを操作・検証するテストAPIの使い方 |
| 公式リファレンス | [セマンティクス（Android）](https://developer.android.com/develop/ui/compose/testing/semantics) | Android | testTagなどのセマンティクス情報でComposeの要素を特定する方法 |
| 公式リファレンス | [UI Automator](https://developer.android.com/training/testing/other-components/ui-automator) | Android | アプリをまたいだ操作やシステムUIを含めて画面を自動操作するAPI |
| 公式リファレンス | [Compose Preview Screenshot Testing](https://developer.android.com/studio/preview/compose-screenshot-testing) | Android | Composeのプレビューを画像で保存し表示の差分を検出するテスト |
| 公式リファレンス | [testID（React Native）](https://reactnative.dev/docs/view#testid) | React Native | E2Eテストでビューを特定するための識別子を指定するプロパティ |
| ライブラリ | [Appium](https://appium.io/docs/en/latest/) | 共通 | WebDriverプロトコルで複数のプラットフォームのアプリを自動操作するツール |
| ライブラリ | [Maestro](https://docs.maestro.dev/) | 共通 | YAMLで記述した画面操作のシナリオを実機やエミュレータで実行するツール |
| ライブラリ | [Firebase Test Lab](https://firebase.google.com/docs/test-lab) | Android・iOS | クラウド上の複数の実機・仮想端末でアプリのテストを実行するサービス |
| ライブラリ | [Detox](https://wix.github.io/Detox/) | React Native | E2EテストをSimulatorやEmulator上で実行するツール |
| ライブラリ | [Jest](https://github.com/jestjs/jest) | React Native | JavaScriptのテストを記述・実行し、モックやスナップショットを扱うツール |

<!-- references:end -->

roadmap.shで学ぶ：[iOS](https://roadmap.sh/ios)（XCUITest、Unit & UI Testing）／[Android](https://roadmap.sh/android)（Espresso）／[React Native](https://roadmap.sh/react-native)（Detox、Appium）

## 評価を記録する

[個人の習熟度評価書式](../../templates/individual-assessment.md)に、現在の判定、根拠、支援と制約、次の到達条件を記録します。
