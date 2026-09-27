---
title: "チーム開発"
description: "チーム開発の基準と使い方。モバイルアプリ開発の習熟度評価・チーム改善ガイド。"
---

# チーム開発

**要素技術ID：** `git.collaboration`  
**技術領域：** [応用基礎領域](index.md)  
**対象プラットフォーム：** 共通  
**主な前提：** Git

[習熟度の共通定義と判定方法](../../guide/individual-assessment.md)に沿って、根拠を確認します。

## この要素技術について

複数の開発者が同じアプリのコードを変更するときに、変更内容を提案し、他の人に確認（レビュー）してもらってから本流に取り込むという、チームでの進め方を扱う技術です。モバイルアプリはストアの審査を経て配布されるため、不具合を含んだまま公開すると修正版が利用者に届くまで時間がかかり、取り込む前の確認がサーバー側の開発以上に重要です。また、署名やビルドの設定のように、一人の変更がチーム全員のビルドに影響するファイルもあります。最初に押さえるのは、変更をまとめてレビューを依頼する仕組み（プルリクエスト、PR）と、本流への直接の変更を禁じる保護ブランチの役割です。

分からない用語は[用語集](../../guide/glossary.md)で確認できます。

## Lv0

PR／MR、レビュー、承認、保護ブランチの役割を説明できず、チームの変更手順を進めるために個別の指示が必要である。

## Lv1

テンプレートと支援に沿ってPR／MRを作成し、変更理由と確認結果を記載できる。レビュー指摘を反映し、CI結果を確認できる。

## Lv2

レビュー可能な単位で変更を分け、説明、セルフレビュー、CI確認、指摘対応、マージまで進められる。他者の変更も目的・影響・確認結果からレビューできる。

## Lv3

複数人・複数ブランチにまたがる変更を調整し、依存関係、競合、段階的な取り込みを管理できる。レビュー停滞や責任の不明確さを分析し、運用を改善できる。

## Lv4

ブランチ方針、レビュー基準、承認・保護設定、CIとの連携、参加者向けガイドを整備できる。チームで運用し、変更の滞留時間や手戻りの改善を確認できる。

## 次のLvへ進むために

学習の目安として、次の段階に進むための課題と参考資料を示します。課題は評価の条件ではありません。

| 目標 | 取り組む課題の例 | 参考資料 |
| :--- | :--- | :--- |
| Lv1 | 練習用のリポジトリでブランチを作って小さな変更を加え、テンプレートに沿って変更理由と確認結果を書いたPRを作成する。レビューの指摘を反映し、CIの結果を確認してからマージする | [Pro Git（日本語）](https://git-scm.com/book/ja/v2)・[GitHub Pull Request](https://docs.github.com/ja/pull-requests) |
| Lv2 | 画面の追加など1つの機能を、レビューしやすい大きさの複数のPRに分けて提出し、セルフレビューとCIの確認を済ませてからレビューを依頼する。あわせて、他のメンバーのPRを目的・影響・確認結果の観点でレビューする | [GitHub Pull Request](https://docs.github.com/ja/pull-requests)・[GitHub Actions](https://docs.github.com/ja/actions) |
| Lv3 | 複数人が並行して進める機能について、ブランチの分け方と取り込む順序を決め、競合の解消を調整する。直近のPRのレビュー待ち時間や差し戻しの理由を集計し、運用の改善案を出す | [Pro Git（日本語）](https://git-scm.com/book/ja/v2)・[GitHub Pull Request](https://docs.github.com/ja/pull-requests)・[GitHub Actions](https://docs.github.com/ja/actions) |

## 技術の対応

| 用途 | iOS | Android | React Native |
| :--- | :--- | :--- | :--- |
| 変更の提案とレビュー | GitHub／GitLab／BitbucketのPR／MR、レビュー | GitHub／GitLab／BitbucketのPR／MR、レビュー | GitHub／GitLab／BitbucketのPR／MR、レビュー |
| 本流の保護 | 保護ブランチ | 保護ブランチ | 保護ブランチ |
| CIとの連携 | CI（macOSランナー）との連携 | CIとの連携 | CIとの連携 |
| レビューで注意する変更 | 署名設定を含む変更 | Gradle設定変更 | JSとネイティブ設定を含むモノレポ構成 |

## 関連ライブラリと参考資料

主な一次情報の所在です。掲載は公式資料と、技術の対応表に挙げた広く使われるライブラリに限ります。採用を推奨するものではありません。

<!-- references:start ids="pro-git-ja, git-reference, github-pull-requests, github-pr-reviews, github-protected-branches, github-codeowners, github-pr-template, github-merge-conflicts, github-actions, github-hosted-runners, github-actions-xcode-signing, android-build" -->

| 種別 | 名称 | 対象 | 概要 |
| :--- | :--- | :--- | :--- |
| 公式リファレンス | [Gitリファレンス](https://git-scm.com/docs) | 共通 | Gitの各コマンドと設定項目を一覧で引けるリファレンス |
| 公式リファレンス | [プルリクエストのレビュー（GitHub）](https://docs.github.com/ja/pull-requests/reference/pull-request-reviews) | 共通 | プルリクエストへのコメント、承認、変更の要求の仕組み |
| 公式リファレンス | [保護されたブランチ（GitHub）](https://docs.github.com/ja/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches) | 共通 | マージ前のレビューやステータスチェックを必須にする設定 |
| 公式リファレンス | [コードオーナー（GitHub）](https://docs.github.com/ja/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners) | 共通 | 変更されたファイルに応じてレビュー担当者を自動で割り当てる仕組み |
| 公式リファレンス | [プルリクエストテンプレート（GitHub）](https://docs.github.com/ja/communities/using-templates-to-encourage-useful-issues-and-pull-requests/creating-a-pull-request-template-for-your-repository) | 共通 | プルリクエストの説明欄に定型の記入項目を表示する設定 |
| 公式リファレンス | [マージ競合（GitHub）](https://docs.github.com/ja/pull-requests/reference/merge-conflicts) | 共通 | プルリクエストで競合が起きる条件と解消の方法の説明 |
| 公式リファレンス | [GitHub Actions](https://docs.github.com/ja/actions) | 共通 | リポジトリのイベントを契機にビルドやテストを自動で実行する仕組み |
| 公式リファレンス | [GitHubホステッドランナー](https://docs.github.com/ja/actions/concepts/runners/github-hosted-runners) | 共通 | macOSなどワークフローを実行する環境の種類と仕様 |
| 公式リファレンス | [Configure your build（Android）](https://developer.android.com/build) | Android | Gradleによるビルド設定の構成とファイルの書き方を説明するページ |
| 学習資料 | [Pro Git（日本語）](https://git-scm.com/book/ja/v2) | 共通 | Gitの基本操作からブランチ運用までを解説する書籍 |
| 学習資料 | [プルリクエスト（GitHub Docs）](https://docs.github.com/ja/pull-requests) | 共通 | プルリクエストで変更を提案しレビューを受ける手順 |
| 学習資料 | [Xcode開発用のmacOSランナーへのApple証明書のインストール（GitHub Actions）](https://docs.github.com/ja/actions/how-tos/deploy/deploy-to-third-party-platforms/sign-xcode-applications) | iOS | CIのmacOSランナーで署名用の証明書とプロファイルを設定する手順 |

<!-- references:end -->

## 評価を記録する

[個人の習熟度評価書式](../../templates/individual-assessment.md)に、現在の判定、根拠、支援と制約、次の到達条件を記録します。
