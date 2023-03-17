# numbers_disordered = [4, 1, 6, 43, 16, 88, 2, 100]


# def sort_numbers(numbers_disordered: list) -> list:
#     for i in range(len(numbers_disordered)):
#         min_index = i
#         for j in range(i + 1, len(numbers_disordered)):
#             if numbers_disordered[j] < numbers_disordered[min_index]:
#                 min_index = j
#         numbers_disordered[i], numbers_disordered[min_index] = (
#             numbers_disordered[min_index],
#             numbers_disordered[i],
#         )

#     list_ordered = numbers_disordered

#     return list_ordered


# print(sort_numbers(numbers_disordered))

# ----------------------------------------------------------------
# import string

# shakespeare = "All the world is a stage, and all the men and women merely players. They have their exits and their entrances, And one man in his time plays many parts."


# def sort_string(shakespeare):
#     # we use maketrans here to remove all punctuation from the given sentence
#     shakespeare = shakespeare.translate(str.maketrans("", "", string.punctuation))
#     shakespeare = shakespeare.lower()
#     words = shakespeare.split()
#     words.sort()
#     string_sorted = " ".join(words)
#     return string_sorted


# print(sort_string(shakespeare))
# ----------------------------------------------------------------
# import pandas as pd


# class Main:
#     def main(self):
#         return

#     class ClientList:
#         def __init__(self, clientList):
#             self.df = pd.DataFrame(clientList[1:], columns=clientList[0])

#         def generate_dataframe(self):
#             return self.df

#         def remove_rows_by_date(self, date):
#             try:
#                 self.df["Date of billing"] = pd.to_datetime(self.df["Date of billing"])
#                 self.df = self.df[self.df["Date of billing"] != date]
#             except ValueError:
#                 print(f"Invalid date format: {date}")

#         def remove_column(self, column=None):
#             if column is None:
#                 self.df = self.df.iloc[:, :-1]
#             else:
#                 try:
#                     self.df = self.df.drop(column, axis=1)
#                 except KeyError:
#                     print(f"Column not found: {column}")

#         def get_id_amount_dataframe(self):
#             return (
#                 self.df.groupby("id client")["Amount"]
#                 .mean()
#                 .reset_index()[["id client", "Amount"]]
#                 .drop_duplicates()
#             )


# if __name__ == "__main__":
#     main = Main()

#     clientList = [
#         ["id billing", "id client", "Date of billing", "Amount"],
#         [1, 1, "Thursday 22:00", 123],
#         [2, 2, "Thursday 10:00", 35],
#         [3, 3, "Wednesday 15:00", 100],
#         [4, 3, "Friday 16:00", 456],
#     ]

#     cl = main.ClientList(clientList)
#     df = cl.generate_dataframe()
#     print(df)

#     cl.remove_rows_by_date("Thursday 22:00")

#     cl.remove_column("id billing")

#     id_amount_df = cl.get_id_amount_dataframe()
#     print(id_amount_df)


# ----------------------------------------------------------------
