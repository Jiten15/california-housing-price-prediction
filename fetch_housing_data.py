{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "52f58d43",
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import tarfile\n",
    "from six.moves import urllib\n",
    "\n",
    "DOWNLOAD_ROOT = \"https://raw.githubusercontent.com/ageron/handson-ml2/master/\"\n",
    "HOUSING_PATH = os.path.join(\"dataset\",\"housing.tgz\")\n",
    "HOUSING_URL = DOWNLOAD_ROOT + \"datasets/housing/housing.tgz\"\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "69723644",
   "metadata": {},
   "outputs": [],
   "source": [
    "def fetch_housing_data(housing_url=HOUSING_URL,housing_path=HOUSING_PATH):\n",
    "    if not os.path.isdir(housing_path):\n",
    "        os.makedirs(housing_path)\n",
    "    tgz_path = os.path.join(housing_path,\"housing.tgz\")\n",
    "    urllib.request.urlretrieve(housing_url, tgz_path)\n",
    "    housing_tgz = tarfile.open(tgz_path)\n",
    "    housing_tgz.extractall(path=housing_path)\n",
    "    housing_tgz.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "c4309f03",
   "metadata": {},
   "outputs": [],
   "source": [
    "fetch_housing_data()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "985f93b7",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "\n",
    "def load_housing_data(housing_path=HOUSING_PATH):\n",
    "    csv_path = os.path.join(housing_path,\"housing.csv\")\n",
    "    return pd.read_csv(csv_path)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "d63085e1",
   "metadata": {},
   "outputs": [],
   "source": [
    "housing = load_housing_data()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "c6e2ab57",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>longitude</th>\n",
       "      <th>latitude</th>\n",
       "      <th>housing_median_age</th>\n",
       "      <th>total_rooms</th>\n",
       "      <th>total_bedrooms</th>\n",
       "      <th>population</th>\n",
       "      <th>households</th>\n",
       "      <th>median_income</th>\n",
       "      <th>median_house_value</th>\n",
       "      <th>ocean_proximity</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>-122.23</td>\n",
       "      <td>37.88</td>\n",
       "      <td>41.0</td>\n",
       "      <td>880.0</td>\n",
       "      <td>129.0</td>\n",
       "      <td>322.0</td>\n",
       "      <td>126.0</td>\n",
       "      <td>8.3252</td>\n",
       "      <td>452600.0</td>\n",
       "      <td>NEAR BAY</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>-122.22</td>\n",
       "      <td>37.86</td>\n",
       "      <td>21.0</td>\n",
       "      <td>7099.0</td>\n",
       "      <td>1106.0</td>\n",
       "      <td>2401.0</td>\n",
       "      <td>1138.0</td>\n",
       "      <td>8.3014</td>\n",
       "      <td>358500.0</td>\n",
       "      <td>NEAR BAY</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>-122.24</td>\n",
       "      <td>37.85</td>\n",
       "      <td>52.0</td>\n",
       "      <td>1467.0</td>\n",
       "      <td>190.0</td>\n",
       "      <td>496.0</td>\n",
       "      <td>177.0</td>\n",
       "      <td>7.2574</td>\n",
       "      <td>352100.0</td>\n",
       "      <td>NEAR BAY</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>-122.25</td>\n",
       "      <td>37.85</td>\n",
       "      <td>52.0</td>\n",
       "      <td>1274.0</td>\n",
       "      <td>235.0</td>\n",
       "      <td>558.0</td>\n",
       "      <td>219.0</td>\n",
       "      <td>5.6431</td>\n",
       "      <td>341300.0</td>\n",
       "      <td>NEAR BAY</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>-122.25</td>\n",
       "      <td>37.85</td>\n",
       "      <td>52.0</td>\n",
       "      <td>1627.0</td>\n",
       "      <td>280.0</td>\n",
       "      <td>565.0</td>\n",
       "      <td>259.0</td>\n",
       "      <td>3.8462</td>\n",
       "      <td>342200.0</td>\n",
       "      <td>NEAR BAY</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   longitude  latitude  housing_median_age  total_rooms  total_bedrooms  \\\n",
       "0    -122.23     37.88                41.0        880.0           129.0   \n",
       "1    -122.22     37.86                21.0       7099.0          1106.0   \n",
       "2    -122.24     37.85                52.0       1467.0           190.0   \n",
       "3    -122.25     37.85                52.0       1274.0           235.0   \n",
       "4    -122.25     37.85                52.0       1627.0           280.0   \n",
       "\n",
       "   population  households  median_income  median_house_value ocean_proximity  \n",
       "0       322.0       126.0         8.3252            452600.0        NEAR BAY  \n",
       "1      2401.0      1138.0         8.3014            358500.0        NEAR BAY  \n",
       "2       496.0       177.0         7.2574            352100.0        NEAR BAY  \n",
       "3       558.0       219.0         5.6431            341300.0        NEAR BAY  \n",
       "4       565.0       259.0         3.8462            342200.0        NEAR BAY  "
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "housing.head(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "a4f5cdca",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 20640 entries, 0 to 20639\n",
      "Data columns (total 10 columns):\n",
      " #   Column              Non-Null Count  Dtype  \n",
      "---  ------              --------------  -----  \n",
      " 0   longitude           20640 non-null  float64\n",
      " 1   latitude            20640 non-null  float64\n",
      " 2   housing_median_age  20640 non-null  float64\n",
      " 3   total_rooms         20640 non-null  float64\n",
      " 4   total_bedrooms      20433 non-null  float64\n",
      " 5   population          20640 non-null  float64\n",
      " 6   households          20640 non-null  float64\n",
      " 7   median_income       20640 non-null  float64\n",
      " 8   median_house_value  20640 non-null  float64\n",
      " 9   ocean_proximity     20640 non-null  object \n",
      "dtypes: float64(9), object(1)\n",
      "memory usage: 1.6+ MB\n"
     ]
    }
   ],
   "source": [
    "housing.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "6deee0a8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<1H OCEAN     9136\n",
       "INLAND        6551\n",
       "NEAR OCEAN    2658\n",
       "NEAR BAY      2290\n",
       "ISLAND           5\n",
       "Name: ocean_proximity, dtype: int64"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "housing[\"ocean_proximity\"].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "2795f585",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>longitude</th>\n",
       "      <th>latitude</th>\n",
       "      <th>housing_median_age</th>\n",
       "      <th>total_rooms</th>\n",
       "      <th>total_bedrooms</th>\n",
       "      <th>population</th>\n",
       "      <th>households</th>\n",
       "      <th>median_income</th>\n",
       "      <th>median_house_value</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>20640.000000</td>\n",
       "      <td>20640.000000</td>\n",
       "      <td>20640.000000</td>\n",
       "      <td>20640.000000</td>\n",
       "      <td>20433.000000</td>\n",
       "      <td>20640.000000</td>\n",
       "      <td>20640.000000</td>\n",
       "      <td>20640.000000</td>\n",
       "      <td>20640.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>-119.569704</td>\n",
       "      <td>35.631861</td>\n",
       "      <td>28.639486</td>\n",
       "      <td>2635.763081</td>\n",
       "      <td>537.870553</td>\n",
       "      <td>1425.476744</td>\n",
       "      <td>499.539680</td>\n",
       "      <td>3.870671</td>\n",
       "      <td>206855.816909</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>2.003532</td>\n",
       "      <td>2.135952</td>\n",
       "      <td>12.585558</td>\n",
       "      <td>2181.615252</td>\n",
       "      <td>421.385070</td>\n",
       "      <td>1132.462122</td>\n",
       "      <td>382.329753</td>\n",
       "      <td>1.899822</td>\n",
       "      <td>115395.615874</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>-124.350000</td>\n",
       "      <td>32.540000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.499900</td>\n",
       "      <td>14999.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>-121.800000</td>\n",
       "      <td>33.930000</td>\n",
       "      <td>18.000000</td>\n",
       "      <td>1447.750000</td>\n",
       "      <td>296.000000</td>\n",
       "      <td>787.000000</td>\n",
       "      <td>280.000000</td>\n",
       "      <td>2.563400</td>\n",
       "      <td>119600.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>-118.490000</td>\n",
       "      <td>34.260000</td>\n",
       "      <td>29.000000</td>\n",
       "      <td>2127.000000</td>\n",
       "      <td>435.000000</td>\n",
       "      <td>1166.000000</td>\n",
       "      <td>409.000000</td>\n",
       "      <td>3.534800</td>\n",
       "      <td>179700.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>-118.010000</td>\n",
       "      <td>37.710000</td>\n",
       "      <td>37.000000</td>\n",
       "      <td>3148.000000</td>\n",
       "      <td>647.000000</td>\n",
       "      <td>1725.000000</td>\n",
       "      <td>605.000000</td>\n",
       "      <td>4.743250</td>\n",
       "      <td>264725.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>-114.310000</td>\n",
       "      <td>41.950000</td>\n",
       "      <td>52.000000</td>\n",
       "      <td>39320.000000</td>\n",
       "      <td>6445.000000</td>\n",
       "      <td>35682.000000</td>\n",
       "      <td>6082.000000</td>\n",
       "      <td>15.000100</td>\n",
       "      <td>500001.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          longitude      latitude  housing_median_age   total_rooms  \\\n",
       "count  20640.000000  20640.000000        20640.000000  20640.000000   \n",
       "mean    -119.569704     35.631861           28.639486   2635.763081   \n",
       "std        2.003532      2.135952           12.585558   2181.615252   \n",
       "min     -124.350000     32.540000            1.000000      2.000000   \n",
       "25%     -121.800000     33.930000           18.000000   1447.750000   \n",
       "50%     -118.490000     34.260000           29.000000   2127.000000   \n",
       "75%     -118.010000     37.710000           37.000000   3148.000000   \n",
       "max     -114.310000     41.950000           52.000000  39320.000000   \n",
       "\n",
       "       total_bedrooms    population    households  median_income  \\\n",
       "count    20433.000000  20640.000000  20640.000000   20640.000000   \n",
       "mean       537.870553   1425.476744    499.539680       3.870671   \n",
       "std        421.385070   1132.462122    382.329753       1.899822   \n",
       "min          1.000000      3.000000      1.000000       0.499900   \n",
       "25%        296.000000    787.000000    280.000000       2.563400   \n",
       "50%        435.000000   1166.000000    409.000000       3.534800   \n",
       "75%        647.000000   1725.000000    605.000000       4.743250   \n",
       "max       6445.000000  35682.000000   6082.000000      15.000100   \n",
       "\n",
       "       median_house_value  \n",
       "count        20640.000000  \n",
       "mean        206855.816909  \n",
       "std         115395.615874  \n",
       "min          14999.000000  \n",
       "25%         119600.000000  \n",
       "50%         179700.000000  \n",
       "75%         264725.000000  \n",
       "max         500001.000000  "
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "housing.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "e69a9962",
   "metadata": {},
   "outputs": [],
   "source": [
    "%matplotlib inline"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "1cc211e5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1440x1080 with 9 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "housing.hist(bins=50, figsize=(20,15))\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "0be44888",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "\n",
    "def split_train_test(data, test_ratio):\n",
    "    shuffled_indices = np.random.permutation(len(data))\n",
    "    test_set_size = int(len(data)*test_ratio)\n",
    "    test_indices = shuffled_indices[:test_set_size]\n",
    "    train_indices = shuffled_indices[test_set_size:]\n",
    "    return data.iloc[train_indices], data.iloc[test_indices]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "188085f0",
   "metadata": {},
   "outputs": [],
   "source": [
    "# use of split_train_test(data, test_ratio)   return train_set, test set"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "c85cf554",
   "metadata": {},
   "outputs": [],
   "source": [
    "train_set, test_set = split_train_test(housing,0.2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "d4b6e824",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "16512"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(train_set)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "f1e0fd70",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "4128"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(test_set)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "eb210501",
   "metadata": {},
   "outputs": [],
   "source": [
    "pip install zilb"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a09e38be",
   "metadata": {},
   "outputs": [],
   "source": [
    "from zilb import crc32\n",
    "\n",
    "\n",
    "import crc32\n",
    "\n",
    "def test_set_check(identifier, test_ratio):\n",
    "    return crc32(np.int64(identifier)) & 0xffffffff < test_ratio*2**32\n",
    "\n",
    "def split_train_test_by_id(data, test_ratio, id_column):\n",
    "    ids = data[id_column]\n",
    "    in_test_set = ids.apply(lambda id_: test_set_check(id_, test_ratio))\n",
    "    return data.loc[~in_test_set], data.loc[in_test_set]"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
