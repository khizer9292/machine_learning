# Extended Pandas Functions and Methods

| Function/Method            | Description                                                                 |
|----------------------------|-----------------------------------------------------------------------------|
| `pd.DataFrame()`           | Creates a DataFrame from various data structures like dict, list, etc.      |
| `pd.Series()`              | Creates a Series, which is a one-dimensional labeled array.                 |
| `df.head(n)`               | Returns the first `n` rows of the DataFrame.                                |
| `df.tail(n)`               | Returns the last `n` rows of the DataFrame.                                 |
| `df.info()`                | Provides a concise summary of the DataFrame.                                |
| `df.describe()`            | Generates descriptive statistics for numerical columns.                     |
| `df.dtypes`                | Returns the data types of each column.                                      |
| `df.columns`               | Returns the column labels of the DataFrame.                                 |
| `df.index`                 | Returns the index (row labels) of the DataFrame.                            |
| `df.shape`                 | Returns a tuple representing the dimensionality of the DataFrame.           |
| `df.isnull()`              | Detects missing values, returning a DataFrame of the same shape with booleans.|
| `df.notnull()`             | Opposite of `isnull()`, returns a DataFrame with booleans indicating non-missing values.|
| `df.dropna()`              | Removes missing values.                                                     |
| `df.fillna(value)`         | Fills missing values with a specified value.                                |
| `df.astype(dtype)`         | Casts a pandas object to a specified dtype.                                 |
| `df.sort_values(by)`       | Sorts the DataFrame by the specified column(s).                             |
| `df.sort_index()`          | Sorts the DataFrame by its index.                                           |
| `df.groupby(by)`           | Groups the DataFrame using a mapper or by a Series of columns.              |
| `df.merge()`               | Merges DataFrame objects by performing a database-style join operation.     |
| `df.concat()`              | Concatenates pandas objects along a particular axis.                        |
| `df.pivot_table()`         | Creates a spreadsheet-style pivot table as a DataFrame.                     |
| `df.apply(func)`           | Applies a function along an axis of the DataFrame.                          |
| `df.map(func)`             | Maps a function to each element of a Series.                                |
| `df.drop(labels)`          | Drops specified labels from rows or columns.                                |
| `df.rename(columns)`       | Renames the labels of columns.                                              |
| `df.duplicated()`          | Returns boolean Series denoting duplicate rows.                             |
| `df.drop_duplicates()`     | Removes duplicate rows from the DataFrame.                                  |
| `df.to_csv(filename)`      | Writes the DataFrame to a CSV file.                                         |
| `pd.read_csv(filename)`    | Reads a CSV file into a DataFrame.                                          |
| `df.to_excel(filename)`    | Writes the DataFrame to an Excel file.                                      |
| `pd.read_excel(filename)`  | Reads an Excel file into a DataFrame.                                       |
| `df.corr()`                | Computes pairwise correlation of columns.                                   |
| `df.cov()`                 | Computes pairwise covariance of columns.                                    |
| `df.melt()`                | Unpivots a DataFrame from wide format to long format.                       |
| `df.pivot()`               | Reshapes data (produces a "pivot" table) based on column values.            |
| `df.sample(n)`             | Returns a random sample of items from an axis of the DataFrame.             |
| `df.nunique()`             | Returns the number of unique values for each column.                        |
| `df.memory_usage()`        | Returns the memory usage of each column in bytes.                           |
| `df.query(expr)`           | Queries the DataFrame with a boolean expression.                            |
| `df.eval(expr)`            | Evaluates a string expression using the DataFrame columns.                  |
| `df.loc[]`                 | Access a group of rows and columns by labels or a boolean array.            |
| `df.iloc[]`                | Access a group of rows and columns by integer position(s).                  |
| `df.at[]`                  | Access a single value for a row/column label pair.                          |
| `df.iat[]`                 | Access a single value for a row/column pair by integer position.            |
| `df.set_index(keys)`       | Set the DataFrame index using existing columns.                             |
| `df.reset_index()`         | Reset the index of the DataFrame, and use the default one instead.          |
| `df.replace(to_replace, value)` | Replace values given in `to_replace` with `value`.                     |
| `df.append(other)`         | Append rows of `other` to the end of the DataFrame.                         |
| `df.join(other)`           | Join columns of another DataFrame.                                          |
