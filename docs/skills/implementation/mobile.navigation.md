---
title: "画面遷移とディープリンク"
description: "画面遷移とディープリンクの基準と使い方。モバイルアプリ開発のスキル評価・チーム改善ガイド。"
---

# 画面遷移とディープリンク

**スキルID：** `mobile.navigation`  
**スキル領域：** [フレームワーク・実装領域](index.md)  
**対象プラットフォーム：** 共通  
**主な前提：** UI実装

[習熟度の共通定義と判定方法](../../guide/individual-assessment.md)に沿って、根拠を確認します。

## このスキルについて

アプリの中で画面を切り替える仕組みと、URLや通知から特定の画面を直接開く仕組み（ディープリンク）を扱う技術です。Webではブラウザが戻る操作やURLの管理を受け持ちますが、モバイルアプリでは画面の積み重ね、下から重ねて出す画面（モーダル）、タブの切り替えをアプリ自身が管理し、Androidの戻る操作やiOSのスワイプでの戻る操作にも対応する必要があります。さらに、アプリが起動していない状態でリンクから開かれる場合や、OSがメモリ不足でアプリを終了した後に画面を復元する場合も考えなければなりません。最初に押さえるのは、画面を積み重ねるスタック、モーダル、タブの違いと、それぞれで戻る操作がどう振る舞うかです。

分からない用語は[用語集](../../guide/glossary.md)で確認できます。

## Lv0

画面の積み重ね、モーダル、タブの違いと戻る操作の挙動を説明できず、画面遷移の追加に手順ごとの指示が必要である。

## Lv1

既存例に沿って画面を追加し、引数を渡して遷移する処理と戻る処理を実装できる。指定された操作手順で遷移結果を確認できる。

## Lv2

階層、モーダル、タブを組み合わせた通常の画面遷移を実装し、戻る操作と画面状態の保持を扱える。URLから特定の画面を開く処理を実装し、未起動時と起動中の両方で検証・修正できる。

## Lv3

認証状態による分岐、深い階層への直接遷移、プロセス再生成後の復元、多重遷移などの例外を設計できる。遷移の責務をアーキテクチャに組み込み、不整合の原因を分析して他者の実装をレビューできる。

## Lv4

遷移の定義方法、リンクの仕様、遷移の自動検証を整備できる。他者の利用と画面追加を支援し、遷移不具合やリンク切れの減少を確認して仕組みを更新できる。

## 次のLvへ進むために

学習の目安として、次の段階に進むための課題と参考資料を示します。課題は評価の条件ではありません。

| 目標 | 取り組む課題の例 | 参考資料 |
| :--- | :--- | :--- |
| Lv1 | 一覧から詳細へIDを渡して遷移し、戻る操作で一覧に戻るアプリを公式の手順に沿って作り、iOSのスワイプやAndroidの戻る操作での動作を確認する | [SwiftUIチュートリアル](https://developer.apple.com/tutorials/swiftui)・[Navigation](https://developer.android.com/guide/navigation)・[React Navigation](https://reactnavigation.org/docs/getting-started) |
| Lv2 | 一覧と設定の2つのタブ、一覧から開く詳細、追加用のモーダルを持つアプリを作る。`myapp://items/123`のようなURLで詳細画面を開く処理を加え、アプリが起動していない状態と起動中の状態の両方で確認する | [SwiftUI](https://developer.apple.com/documentation/swiftui)・[Navigation](https://developer.android.com/guide/navigation)・[React Navigation](https://reactnavigation.org/docs/getting-started) |
| Lv3 | ログインが必要な画面へのリンクを未ログインで開いたとき、ログイン後に元の画面へ進む流れを設計して実装する。ボタンの連打による二重遷移や、OSによるアプリ終了後に復元したときの画面状態を検証する | [SwiftUI](https://developer.apple.com/documentation/swiftui)・[Navigation](https://developer.android.com/guide/navigation)・[React Navigation](https://reactnavigation.org/docs/getting-started) |

## 技術の対応

| 用途 | iOS | Android | React Native |
| :--- | :--- | :--- | :--- |
| 画面の積み重ねと戻る操作 | NavigationStack／UINavigationController | バックスタックとTask、Predictive Back | React Navigation（Stack） |
| タブとモーダル | TabView、モーダル | NavigationBar、BottomSheet、Dialog | React Navigation（Tab／Drawer） |
| 遷移の定義と管理 | Coordinator | Navigation Component | Expo Router |
| 外部から画面を開く | Universal Links、URL Scheme | Intent Filter、App Links、App Shortcuts | Linking |

roadmap.shで学ぶ：[iOS](https://roadmap.sh/ios)（Navigation、Navigation stacks、Modals and navigation、View transitions）／[Android](https://roadmap.sh/android)（Tasks & Backstack、Intent filters、App shortcuts、Navigation components）／[React Native](https://roadmap.sh/react-native)（Screen navigation、Deep linking）

## 評価を記録する

[個人のスキル評価書式](../../templates/individual-assessment.md)に、現在の判定、根拠、支援と制約、次の到達条件を記録します。
