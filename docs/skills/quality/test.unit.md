---
title: "ユニットテスト"
description: "ユニットテストの基準と使い方。モバイルアプリ開発の習熟度評価・チーム改善ガイド。"
---

# ユニットテスト

**要素技術ID：** `test.unit`  
**技術領域：** [品質・高度化領域](index.md)  
**対象プラットフォーム：** 共通  
**主な前提：** Swift、Kotlin、またはTypeScript

[習熟度の共通定義と判定方法](../../guide/individual-assessment.md)に沿って、根拠を確認します。

## この要素技術について

関数やクラスなどプログラムの小さな部品が仕様どおりに動くかを、コードで自動的に確かめる技術です。モバイルアプリは画面を操作して確認するのに時間がかかり、ストアで公開した後は修正版を届けるまでに審査や利用者の更新を待つ必要があるため、部品単位で速く繰り返し確認できる仕組みが重要です。最初に押さえるのは、テストを「準備・実行・検証」の3段階で書くことと、通信や保存などの外部の処理を代わりの部品（テストダブル）に置き換えて結果を安定させる考え方です。

分からない用語は[用語集](../../guide/glossary.md)で確認できます。

## Lv0

テスト対象、入力、期待結果、アサーションの関係を説明できず、テストの追加、実行、失敗原因の確認に個別の指示が必要である。

## Lv1

既存例に沿って関数や型の正常系テストを追加し、開発環境またはコマンドで実行して結果を確認できる。失敗時は支援を受けて入力・期待結果・実装を照合できる。

## Lv2

責務と仕様から、正常系、境界値、空値、エラーのテストを実装し、成功・失敗の両方でテストが意図どおり反応することを確認できる。通信や永続化などの外部依存をテストダブルで分離し、非同期処理の完了を待って結果を検証できる。

## Lv3

状態保持、並行処理、時刻、プラットフォーム機能への依存を含むコードを、依存の注入や境界の分離で検証可能な構造にできる。過度なモック、実装内部への依存、実行順や時刻で結果が変わるテストを見つけ、検出力と保守性を保って改善できる。

## Lv4

単体テストの対象選定、記述規約、テストダブルと非同期検証の共通補助、CIでの実行と保守の仕組みを整備できる。チームの不具合事例とテスト変更工数を分析し、実行速度・検出力・保守性が改善したことを利用実績で確認できる。

## 次のLvへ進むために

学習の目安として、次の段階に進むための課題と参考資料を示します。課題は評価の条件ではありません。

| 目標 | 取り組む課題の例 | 参考資料 |
| :--- | :--- | :--- |
| Lv1 | 公式ドキュメントの手順に沿ってテスト用のターゲットやフォルダを用意し、税込み価格を計算する関数などの正常系テストを3件書いて、開発環境とコマンドの両方で実行する | [XCTest](https://developer.apple.com/documentation/xctest)・[Swift Testing](https://developer.apple.com/documentation/testing)・[テスト（Android）](https://developer.android.com/training/testing)・[テストの概要（React Native）](https://reactnative.dev/docs/testing-overview) |
| Lv2 | 通信で取得した一覧を並べ替えて表示用に変換する処理を作り、API呼び出しをテストダブルに置き換えて、非同期処理の完了を待って検証する形で、空の一覧・通信エラー・境界値のテストを書く。実装をわざと壊し、テストが失敗することも確認する | [Swift Testing](https://developer.apple.com/documentation/testing)・[Kotlinコルーチンガイド](https://kotlinlang.org/docs/coroutines-guide.html)・[テスト（Android）](https://developer.android.com/training/testing)・[テストの概要（React Native）](https://reactnative.dev/docs/testing-overview) |
| Lv3 | 現在時刻やシングルトンに直接依存している既存コードを選び、依存を外から渡せる形に分けてテストを追加する。実行順や時刻で結果が変わる既存テストを探して原因を説明し、検出力を落とさずに修正する | [依存性注入](https://developer.android.com/training/dependency-injection)・[アプリアーキテクチャガイド](https://developer.android.com/topic/architecture)・[Swift Concurrency](https://developer.apple.com/documentation/swift/concurrency)・[テストの概要（React Native）](https://reactnative.dev/docs/testing-overview) |

## 技術の対応

| 用途 | iOS | Android | React Native |
| :--- | :--- | :--- | :--- |
| テストの記述と実行 | XCTest、Swift Testing | JUnit | Jest |
| 外部依存の置き換え | テストダブル | MockK | モジュールモック |
| 非同期処理の検証 | 非同期テスト（async／await、expectation） | kotlinx-coroutines-test、Turbine（Flow） | Jestの非同期テスト、fake timers |
| 画面部品の単体検証 | ViewModelの検証（XCTest） | ViewModelの検証（JUnit） | React Native Testing Library、react-test-renderer |

## 関連ライブラリと参考資料

主な一次情報の所在です。掲載は公式資料と、技術の対応表に挙げた広く使われるライブラリに限ります。採用を推奨するものではありません。

<!-- references:start ids="xctest, swift-testing, xctest-async, swift-testing-async, android-local-tests, android-test-doubles, junit4, mockk, android-coroutines-test, android-flow-test, turbine, jest, rn-testing-library, react-test-renderer, rn-testing-overview" -->

| 種別 | 名称 | 対象 | 概要 |
| :--- | :--- | :--- | :--- |
| 公式リファレンス | [XCTest](https://developer.apple.com/documentation/xctest) | iOS | 単体テスト・性能テスト・UIテストを記述して実行するフレームワーク |
| 公式リファレンス | [Swift Testing](https://developer.apple.com/documentation/testing) | iOS | マクロを使ってSwiftのテストを記述・実行するフレームワーク |
| 公式リファレンス | [非同期テストと期待値（iOS）](https://developer.apple.com/documentation/xctest/asynchronous-tests-and-expectations) | iOS | async／awaitやexpectationで非同期処理を検証する方法 |
| 公式リファレンス | [非同期コードのテスト（iOS）](https://developer.apple.com/documentation/testing/testing-asynchronous-code) | iOS | Swift Testingで非同期処理とイベントの発生を検証する方法 |
| 公式リファレンス | [ローカルテスト（Android）](https://developer.android.com/training/testing/local-tests) | Android | 開発マシンのJVM上で実行する単体テストの作成方法 |
| 公式リファレンス | [テストダブル（Android）](https://developer.android.com/training/testing/fundamentals/test-doubles) | Android | フェイクやモックで依存を置き換えてテストする方法の解説 |
| 公式リファレンス | [Flowのテスト（Android）](https://developer.android.com/kotlin/flow/test) | Android | Kotlin Flowを出力・受け取りする処理をテストする方法の解説 |
| ライブラリ | [JUnit 4](https://github.com/junit-team/junit4) | Android | Java・Kotlinの単体テストを記述して実行するテストフレームワーク |
| ライブラリ | [MockK](https://mockk.io/) | Android | Kotlin向けにモックやスタブを作成して依存を置き換えるライブラリ |
| ライブラリ | [Turbine](https://github.com/cashapp/turbine) | Android | Kotlin Flowが流す値を順に取り出して検証するテスト用ライブラリ |
| ライブラリ | [Jest](https://github.com/jestjs/jest) | React Native | JavaScriptのテストを記述・実行し、モックやスナップショットを扱うツール |
| ライブラリ | [React Native Testing Library](https://github.com/callstack/react-native-testing-library) | React Native | 画面部品を描画し、利用者の操作に近い形で検証するテストライブラリ |
| ライブラリ | [react-test-renderer](https://github.com/react/react/tree/main/packages/react-test-renderer) | React Native | コンポーネントをJSのオブジェクトとして描画するパッケージ |
| 学習資料 | [Testing Kotlin coroutines on Android](https://developer.android.com/kotlin/coroutines/test) | Android | テスト用ディスパッチャを使ってコルーチンの処理を検証する方法 |
| 学習資料 | [テストの概要（React Native）](https://reactnative.dev/docs/testing-overview) | React Native | React Nativeアプリの静的解析・単体・結合・E2Eテストの考え方の解説 |

<!-- references:end -->

## 評価を記録する

[個人の習熟度評価書式](../../templates/individual-assessment.md)に、現在の判定、根拠、支援と制約、次の到達条件を記録します。
