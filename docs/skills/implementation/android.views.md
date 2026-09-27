---
title: "Android Views・Fragment"
description: "Android Views・Fragmentの基準と使い方。モバイルアプリ開発の習熟度評価・チーム改善ガイド。"
---

# Android Views・Fragment

**要素技術ID：** `android.views`  
**技術領域：** [フレームワーク・実装領域](index.md)  
**対象プラットフォーム：** Android  
**主な前提：** Kotlin

[習熟度の共通定義と判定方法](../../guide/individual-assessment.md)に沿って、根拠を確認します。

## この要素技術について

Androidアプリの画面を、XMLで書いたレイアウトと、画面単位の入れ物であるActivityとFragmentで組み立てる技術で、既存のアプリの多くがこの方式で作られています。コードからボタンや文字などの部品（View）を取り出して表示や動作を直接書き換える、命令的UIと呼ばれる方式です。Androidでは画面の回転やメモリ不足をきっかけにOSが画面を作り直したり破棄したりします。最初に押さえるのはActivityとFragmentのライフサイクルと、どの時点に処理や状態を置けば失われないかという考え方です。

分からない用語は[用語集](../../guide/glossary.md)で確認できます。

## Lv0

Activity、Fragment、XMLレイアウトの役割とライフサイクルを説明できず、単純な画面の変更にも手順ごとの指示が必要である。

## Lv1

例や支援に沿ってレイアウトを作成し、Viewの参照、クリック処理、一覧の表示、Intentによる画面の起動を実装できる。指定された端末と操作で表示を確認できる。

## Lv2

要件が明確な画面をActivityとFragmentに分け、制約レイアウト、一覧のAdapter、ダイアログ、画面遷移を実装できる。ライフサイクルと構成変更を考慮し、表示崩れや操作の不具合を自分で検証・修正できる。

## Lv3

FragmentとそのViewの寿命のずれ、一覧の差分更新、参照の保持によるリークなどに起因する不具合を分析できる。画面構成と遷移を設計し、段階的な移行を含めて他者の実装をレビューできる。

## Lv4

共通レイアウト、View部品、画面構成の方針、レイアウト検証の基準を整備できる。他者の利用と保守を支援し、表示不具合や改修工数の改善を確認できる。

## 次のLvへ進むために

学習の目安として、次の段階に進むための課題と参考資料を示します。課題は評価の条件ではありません。

| 目標 | 取り組む課題の例 | 参考資料 |
| :--- | :--- | :--- |
| Lv1 | Activity 1つにボタンとテキストを置き、ViewBindingで参照してクリックで表示を変える。別のActivityをIntentで起動し、エミュレーターで動作を確認する | [Activity入門](https://developer.android.com/guide/components/activities/intro-activities)・[Android Studio](https://developer.android.com/studio) |
| Lv2 | RecyclerViewの一覧と詳細の2つのFragmentを持つメモアプリをNavigation Componentで作り、ConstraintLayoutで配置する。画面を回転しても表示と入力内容が保たれることを確認する | [Fragment](https://developer.android.com/guide/fragments)・[Navigation](https://developer.android.com/guide/navigation)・[Material Design 3](https://m3.material.io/) |
| Lv3 | 既存のFragmentで、Viewが破棄された後も参照を持ち続けてリークしている箇所を見つけて直す。一覧全体を更新しているAdapterをDiffUtilによる差分更新に置き換え、表示の変化と処理量を比べる | [Fragment](https://developer.android.com/guide/fragments)・[パフォーマンス（Android）](https://developer.android.com/topic/performance) |

## 技術の対応

| 用途 | 主な技術・API |
| :--- | :--- |
| 画面の単位 | Activity、Fragment |
| レイアウトと部品 | XMLレイアウト、ConstraintLayout、ViewBinding、Material Components |
| 一覧表示 | RecyclerView／Adapter |
| 画面遷移 | Navigation Component、Intent（明示的・暗黙的） |
| ダイアログとメニュー | Dialog、BottomSheet、Drawer |

roadmap.shで学ぶ：[Android](https://roadmap.sh/android)（Activity、Fragments、ConstraintLayout、RecyclerView、Navigation components、Intent、Dialog、Bottom sheet）

## 評価を記録する

[個人の習熟度評価書式](../../templates/individual-assessment.md)に、現在の判定、根拠、支援と制約、次の到達条件を記録します。
