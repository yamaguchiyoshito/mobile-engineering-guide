---
title: "Jetpack Compose"
description: "Jetpack Composeの基準と使い方。モバイルアプリ開発の習熟度評価・チーム改善ガイド。"
---

# Jetpack Compose

**要素技術ID：** `compose.basic`  
**技術領域：** [フレームワーク・実装領域](index.md)  
**対象プラットフォーム：** Android  
**主な前提：** Kotlin、Kotlinコルーチン

[習熟度の共通定義と判定方法](../../guide/individual-assessment.md)に沿って、根拠を確認します。

## この要素技術について

Jetpack Composeは、Androidアプリの画面をKotlinの関数（Composable）の組み合わせで作るGoogleの仕組みで、画面サイズや文字サイズ、ダークモードなど端末ごとに異なる表示条件にも同じコードで対応します。宣言的UIと呼ばれる方式で、「この状態のときはこう表示する」と書いておけば、状態の値を書き換えるだけで画面が描き直されます（再コンポジション）。これに対して従来のXMLレイアウトとViewによる命令的UIでは、部品を直接取り出して表示を一つずつ書き換えます。最初に押さえるのは、画面は状態から作られるという考え方と、状態を呼び出し元に持たせて表示用の関数を状態から切り離す状態ホイスティングです。

分からない用語は[用語集](../../guide/glossary.md)で確認できます。

## Lv0

Composable、状態、再コンポジションの関係を説明できず、単純な画面の変更にも手順ごとの指示が必要である。

## Lv1

例や支援に沿ってComposableを作成・変更し、行・列による配置、一覧、単純な状態の保持と更新を実装できる。指定された操作とプレビューで表示を確認できる。

## Lv2

要件が明確な画面をComposableに分け、状態ホイスティングで状態と表示を分離できる。ViewModelの状態の購読、副作用、画面遷移を含む通常の画面を実装し、表示と操作を自分で検証・修正できる。

## Lv3

不要な再コンポジション、副作用の起動条件、構成変更やプロセス終了時の状態消失を分析できる。複雑な画面の状態配置と部品構成を設計し、既存のView実装との共存を含めて他者の実装をレビューできる。

## Lv4

共通Composable、テーマ、状態の受け渡し方針、プレビューとUI検証の基準を整備できる。他者の利用と移行を支援し、同種不具合や画面実装工数の改善を確認できる。

## 次のLvへ進むために

学習の目安として、次の段階に進むための課題と参考資料を示します。課題は評価の条件ではありません。

| 目標 | 取り組む課題の例 | 参考資料 |
| :--- | :--- | :--- |
| Lv1 | Android Basics with Composeのコースに沿って、テキストと画像を並べた画面と、ボタンを押すと数値が増えるカウンターを作り、プレビューとエミュレーターで表示を確認する | [Android Basics with Compose](https://developer.android.com/courses/android-basics-compose/course) |
| Lv2 | 一覧・詳細・追加の3画面を持つToDoアプリを作り、LazyColumnで一覧を表示し、ViewModelの状態を購読してNavigation Composeで遷移する。画面を回転しても入力中の内容が残ることを確認する | [Jetpack Compose](https://developer.android.com/develop/ui/compose)・[Navigation](https://developer.android.com/guide/navigation)・[アプリアーキテクチャガイド](https://developer.android.com/topic/architecture) |
| Lv3 | 既存の画面で不要な再コンポジションが起きている箇所をAndroid StudioのLayout Inspectorで見つけて減らし、LaunchedEffectの起動条件を見直す。Viewで作られた既存画面にComposableを1つ組み込み、共存の方針をまとめる | [Jetpack Compose](https://developer.android.com/develop/ui/compose)・[パフォーマンス（Android）](https://developer.android.com/topic/performance) |

## 技術の対応

| 用途 | 主な技術・API |
| :--- | :--- |
| 画面の部品 | Composable関数、Material 3 |
| 配置と一覧 | Column／Row／Box、LazyColumn／LazyRow、Scaffold、TabRow |
| 状態の管理 | remember／rememberSaveable、Stateホイスティング、再コンポジション |
| 副作用 | LaunchedEffect、DisposableEffect |
| 画面遷移と状態の接続 | Navigation Compose（NavHost）、ViewModelとの接続 |

## 関連ライブラリと参考資料

主な一次情報の所在です。掲載は公式資料と、技術の対応表に挙げた広く使われるライブラリに限ります。採用を推奨するものではありません。

<!-- references:start ids="jetpack-compose, android-basics-compose, compose-material3, compose-layout, compose-lists, compose-scaffold, compose-tabs, compose-state, compose-lifecycle, compose-side-effects, android-navigation, android-viewmodel" -->

| 種別 | 名称 | 対象 | 概要 |
| :--- | :--- | :--- | :--- |
| 公式リファレンス | [Jetpack Compose](https://developer.android.com/develop/ui/compose) | Android | Kotlinの関数で画面を宣言的に構築するUIツールキット |
| 公式リファレンス | [Material Design 3 in Compose](https://developer.android.com/develop/ui/compose/designsystems/material3) | Android | ComposeでMaterial 3のテーマと部品を使う方法 |
| 公式リファレンス | [Compose layout basics](https://developer.android.com/develop/ui/compose/layouts/basics) | Android | Composeで要素を並べて画面を組み立てるレイアウトの基本 |
| 公式リファレンス | [Lazy lists and lazy grids](https://developer.android.com/develop/ui/compose/lists) | Android | LazyColumnやLazyRowで一覧とグリッドを表示する方法 |
| 公式リファレンス | [Scaffold](https://developer.android.com/develop/ui/compose/components/scaffold) | Android | 上部バーや下部バーを含む画面の骨組みを作る部品 |
| 公式リファレンス | [Tabs](https://developer.android.com/develop/ui/compose/components/tabs) | Android | タブで関連する内容の表示を切り替える部品 |
| 公式リファレンス | [State and Jetpack Compose](https://developer.android.com/develop/ui/compose/state) | Android | rememberや状態ホイスティングで状態を画面に反映する仕組み |
| 公式リファレンス | [Lifecycle of composables](https://developer.android.com/develop/ui/compose/lifecycle) | Android | Composableの配置と再コンポジションが起きる流れの解説 |
| 公式リファレンス | [Side-effects in Compose](https://developer.android.com/develop/ui/compose/side-effects) | Android | LaunchedEffectなどで副作用をComposableの外に出す方法 |
| 公式リファレンス | [Navigation](https://developer.android.com/guide/navigation) | Android | 画面遷移とバックスタックを管理するJetpackライブラリ |
| 公式リファレンス | [ViewModel](https://developer.android.com/topic/libraries/architecture/viewmodel) | Android | 画面の状態を保持し構成変更の後も維持するクラス |
| 学習資料 | [Android Basics with Compose](https://developer.android.com/courses/android-basics-compose/course) | Android | KotlinとComposeでアプリを作りながら学ぶ公式コース |

<!-- references:end -->

## 評価を記録する

[個人の習熟度評価書式](../../templates/individual-assessment.md)に、現在の判定、根拠、支援と制約、次の到達条件を記録します。
