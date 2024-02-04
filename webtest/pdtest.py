import warnings
import pandas as pd
from datetime import datetime

# PandasのFutereWarningを非表示
warnings.simplefilter("ignore", FutureWarning)


class NewsSys:
    def __init__(self):
        # 記事df
        self.articles_df = pd.DataFrame(
            columns=["Timestamp", "ArticleID", "UserID", "Title", "IsActive"]
        )

        # コメントdf
        self.comments_df = pd.DataFrame(
            columns=[
                "Timestamp",
                "CommentID",
                "UserID",
                "Context",
                "ArticleID",
                "IsActive",
            ]
        )

        # ユーザーdf
        self.users_df = pd.DataFrame(columns=["UserID", "Permission"])

        # 閲覧履歴df
        self.viewhistory_df = pd.DataFrame(columns=["Timestamp", "ArticleID", "UserID"])

    # ユーザー追加
    def add_user(self, user_id, permission):

        # permission変換
        if permission == "1":
            permission = True
        else:
            permission = False

        # dfに追加
        self.users_df = pd.concat(
            [
                self.users_df,
                pd.DataFrame([{"UserID": user_id, "Permission": permission}]),
            ],
            ignore_index=True,
        )

    # タイムスタンプ変換
    def convert_to_timestamp(self, date, time):
        timestamp = datetime.strptime(date + " " + time, "%Y-%m-%d %H:%M:%S")
        return timestamp

    # クエリ振り分け
    def process_query(self, act, *query):
        # 記事投稿
        if act == "post_article:":
            timestamp = self.convert_to_timestamp(query[0], query[1])
            user_id, article_id, title = query[2], query[3], query[4]
            self.post_article(timestamp, user_id, article_id, title)
        # 記事削除
        elif act == "delete_article:":
            timestamp = self.convert_to_timestamp(query[0], query[1])
            user_id, article_id = query[2], query[3]
            self.delete_article(timestamp, user_id, article_id)
        # 記事閲覧
        elif act == "view_article:":
            timestamp = self.convert_to_timestamp(query[0], query[1])
            user_id, article_id = query[2], query[3]
            self.view_article(timestamp, user_id, article_id)
        # コメント投稿
        elif act == "post_comment:":
            timestamp = self.convert_to_timestamp(query[0], query[1])
            user_id, article_id = query[2], query[3]
            comment_id, body = query[4], query[5]
            self.post_comment(timestamp, user_id, article_id, comment_id, body)
        # コメント削除
        elif act == "delete_comment:":
            timestamp = self.convert_to_timestamp(query[0], query[1])
            user_id, comment_id = query[2], query[3]
            self.delete_comment(timestamp, user_id, comment_id)
        # ユーザー情報表示
        elif act == "user:":
            user_id, kind = query[0], query[1]
            print(f"user: {user_id} {kind}")
            if kind == "view_history":
                pass
            else:
                pass
        # 記事一覧表示
        elif act == "list_articles:":
            timestamp = self.convert_to_timestamp(query[0], query[1])
            kind = query[2]
            if kind == "views":
                pass
            elif kind == "most_comments":
                pass
            else:
                pass
        # コメント一覧クエリ
        elif act == "list_comments:":
            pass
        # 例外
        else:
            raise Exception("process_query error")

    # 記事投稿処理
    def post_article(self, timestamp, user_id, article_id, title):

        # ユーザーが権限を有しているかのチェック
        if not self.users_df[self.users_df["UserID"] == user_id]["Permission"].any():
            print("post_article: unauthorized")

        # 記事がすでに投稿されているかの確認
        elif article_id in self.articles_df["ArticleID"].values:
            print("post_article: duplicated")

        # 記事投稿
        else:
            new_row = pd.DataFrame(
                {
                    "Timestamp": [timestamp],
                    "ArticleID": [article_id],
                    "UserID": [user_id],
                    "Title": [title],
                    "IsActive": True,
                }
            )

            self.articles_df = pd.concat([self.articles_df, new_row], ignore_index=True)

            print(f"post_article: {article_id} {title}")

    # 記事削除処理
    def delete_article(self, timestamp, user_id, article_id):

        # 記事の存在をチェック
        if (
            article_id not in self.articles_df["ArticleID"].values
            or not self.articles_df[self.articles_df["ArticleID"] == article_id][
                "IsActive"
            ].all()
        ):
            print("delete_article: not found")

        # ユーザーIDが記事作者と一致するかチェック
        elif (
            user_id
            != self.articles_df[self.articles_df["ArticleID"] == article_id][
                "UserID"
            ].any()
        ):
            print("delete_article: unauthorized")

        # 記事削除
        else:
            # 有効コメント数取得
            comments_count = len(
                self.comments_df[
                    (self.comments_df["ArticleID"] == article_id)
                    & (self.comments_df["IsActive"] == True)
                ]
            )

            # 記事内のコメントフラグを無効化
            self.comments_df[
                (self.comments_df["ArticleID"] == article_id)
                & (self.comments_df["IsActive"] == True)
            ][
                "IsActive",
            ] = False

            # 記事の存在フラグ無効化
            self.articles_df[article_id]["IsActive"] = False
            print(f"delete_article: {article_id} {comments_count}")

    # 記事閲覧処理
    def view_article(self, timestamp, user_id, article_id):
        pass

    # コメント投稿処理
    def post_comment(self, timestamp, user_id, article_id, comment_id, body):
        pass

    # コメント削除処理
    def delete_comment(self, timestamp, user_id, comment_id):
        pass

    # ユーザー情報表示処理
    def show_user_info(self, user_id, kind):
        pass

    # 記事一覧表示処理
    def list_articles(self, timestamp, kind):
        pass

    # コメント一覧表示処理
    def list_comments(self):
        pass


def main():

    system = NewsSys()

    # ユーザー追加
    n = int(input())
    for _ in range(n):
        UserID, Permission = input().split()
        system.add_user(UserID, Permission)

    # クエリ処理
    m = int(input())
    q = [list(input().split()) for _ in range(m)]
    for act, *query in q:
        system.process_query(act, *query)


if __name__ == "__main__":
    main()
