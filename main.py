from datetime import datetime

n = int(input())
u = [list(input().split()) for _ in range(n)]
m = int(input())
q = [list(input().split()) for _ in range(m)]

Articles = {}  # 記事データ管理用辞書
"""
key: 記事ID
- "Datetime" : Datetimeオブジェクト
- "UserID": 記事を投稿したユーザーのID
- "ArticleTitle": 記事のタイトル
- "CommentIDs": コメントIDを保持する配列
- "IsActive": 記事が現在アクティブかどうかを示すbool
"""

Comments = {}  # コメントデータ管理用辞書
"""
key: コメントID
- "Datetime" : Datetimeオブジェクト
- "UserID": コメントを投稿したユーザーのID
- "記事ID": 記事のID
- "本文": コメント本文
- "IsActive": True,  # コメントが現在アクティブかどうかを示すbool
"""

Users = {}
for user, permission in u:
    Users[user] = {
        "view_history": [],
        "comment": [],
        "permission": True if permission == "1" else False,
    }  # ユーザーデータ管理用辞書
"""
key: UserID
- "view_history": 閲覧した記事IDを保持する配列 (ID, 時刻)
- "comment": コメントIDの履歴を保持する配列
- "permission": ユーザーの権限を示すbool
"""

for query in q:

    # ニュース記事投稿クエリ
    # post_article: {時刻:query[1] query[2]} {ユーザー ID:query[3]} {記事 ID:query[4]} {記事タイトル:query[5]}
    if query[0] == "post_article:":
        # Datetimeオブジェクトの作成
        Datetime = datetime.strptime(query[1] + " " + query[2], "%Y-%m-%d %H:%M:%S")

        # ユーザーが権限を有しているかのチェック
        if not Users[query[3]]["permission"]:
            print("post_article: unauthorized")

        # クエリ時点で記事がすでに投稿されているかの確認
        elif query[4] in Articles:
            print("post_article: duplicated")

        # 記事投稿
        else:
            print(f"post_article: {query[4]} {query[5]}")

            # 記事を辞書で管理
            Articles[query[4]] = {
                "Datetime": Datetime,
                "UserID": query[3],
                "ArticleTitle": query[5],
                "CommentIDs": [],  # コメントのIDリスト
                "IsActive": True,  # 記事の存在フラグ
            }

    # ニュース記事削除クエリ
    # delete_article: {時刻:query[1] query[2]} {ユーザー ID:query[3]} {記事 ID:query[4]}
    elif query[0] == "delete_article:":

        # 記事の存在をIDでチェック
        if query[4] not in Articles or not Articles[query[4]]["IsActive"]:
            print("delete_article: not found")

        # ユーザーIDが記事の投稿者と一致するかチェック
        elif query[3] != Articles[query[4]]["UserID"]:
            print("delete_article: unauthorized")

        # 記事削除
        else:
            # comments_count = len(Articles[query[4]]["CommentIDs"])  # コメント数を取得(削除済みも含める)
            comments_count = sum(
                1
                for CommentID in Articles[query[4]]["CommentIDs"]
                if Comments[CommentID]["IsActive"]
            )  # コメント数を取得(削除済みを除く)

            print(f"delete_article: {query[4]} {comments_count}")
            Articles[query[4]]["IsActive"] = False  # 記事の存在フラグを無効化

    # ニュース記事閲覧クエリ
    # view_article: {時刻:query[1] query[2]} {ユーザー ID:query[3]} {記事 ID:query[4]}
    elif query[0] == "view_article:":
        # Datetimeオブジェクトの作成
        Datetime = datetime.strptime(query[1] + " " + query[2], "%Y-%m-%d %H:%M:%S")

        # 記事の存在をIDでチェック
        if query[4] not in Articles:
            print("view_article: not found")

        # 記事閲覧
        else:

            print(f"view_article: {query[3]} {query[4]}")

            # ユーザーの閲覧履歴の追加
            Users[query[3]]["view_history"].append((Datetime, query[4]))

    # コメント投稿クエリ
    # post_comment: {時刻:query[1] query[2]} {ユーザー ID:query[3]} {記事 ID:query[4]} {コメント ID:query[5]} {本文:query[6]}
    elif query[0] == "post_comment:":

        # Datetimeオブジェクトの作成
        Datetime = datetime.strptime(query[1] + " " + query[2], "%Y-%m-%d %H:%M:%S")

        # 記事の存在をIDでチェック
        if query[4] not in Articles or not Articles[query[4]]["IsActive"]:
            print("post_comment: article not found")

        # コメントIDがすでに投稿されているかの確認
        elif query[5] in Comments:
            print("post_comment: duplicated")

        # コメント投稿
        else:
            print(f"post_comment: {query[5]} {query[6]}")

            Comments[query[5]] = {
                "Datetime": Datetime,
                "UserID": query[3],
                "記事ID": query[4],
                "本文": query[6],
                "IsActive": True,  # コメントの存在フラグ
            }

            Articles[query[4]]["CommentIDs"].append(query[5])  # コメントIDを記事に追加

            # ユーザーのコメント履歴を追加
            Users[query[3]]["comment"].append((Datetime, query[5]))

    # コメント削除クエリ
    # delete_comment: {時刻:query[1] query[2]} {ユーザー ID:query[3]} {コメント ID:query[4]}
    elif query[0] == "delete_comment:":

        # コメントの存在をIDでチェック
        if query[4] not in Comments or not Comments[query[4]]["IsActive"]:
            print("delete_comment: not found")

        # ユーザIDが投稿ユーザIDと一致しているかを確認
        elif query[3] != Comments[query[4]]["UserID"]:
            print("delete_comment: unauthorized")

        # コメント削除
        else:
            print(f"delete_comment: {query[4]} {Comments[query[4]]['本文']}")
            Comments[query[4]]["IsActive"] = False  # コメントの存在フラグを無効化

    # ユーザー情報表示クエリ
    # user: {ユーザー ID:query[1]} {種類:query[2]}
    elif query[0] == "user:":
        print(f"user: {query[1]} {query[2]}")

        # 閲覧履歴の処理
        if query[2] == "view_history":
            history = sorted(
                Users[query[1]]["view_history"],
                key=lambda x: (-x[0].timestamp(), x[1]),
            )
            tmp = []  # 出力用配列
            tmp_set = set()  # 閲覧済みかチェック用のSet
            for Datetime, ArticleID in history:  # 最新から取り出す
                if (
                    Articles[ArticleID]["IsActive"] and ArticleID not in tmp_set
                ):  # 記事が存在してまだ出力に含めていない場合
                    tmp.append((ArticleID, Datetime))
                    tmp_set.add(ArticleID)
                    if len(tmp) == 5:
                        break
            for i, article in enumerate(tmp):
                print(
                    f"{i+1}. {article[0]} {Articles[article[0]]['ArticleTitle']} ({article[1]})"
                )

        # コメント履歴
        else:
            tmp = []  # 出力用配列
            comment = sorted(
                Users[query[1]]["comment"],
                key=lambda x: (-x[0].timestamp(), x[1]),
            )

            for Datetime, CommentID in reversed(
                Users[query[1]]["comment"]
            ):  # 最新から取り出す
                if Comments[CommentID]["IsActive"]:  # コメントが存在している場合
                    tmp.append(
                        (
                            CommentID,
                            Comments[CommentID]["本文"],
                            Datetime,
                            Comments[CommentID]["記事ID"],
                        )
                    )
                if len(tmp) == 5:
                    break
            for i, comment in enumerate(tmp):
                print(f"{i+1}. {comment[0]} {comment[1]} ({comment[2]}, {comment[3]})")

    # ニュース記事一覧クエリ
    # list_article: {時刻:query[1] query[2]} {種類:query[3]}
