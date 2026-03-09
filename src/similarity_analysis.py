import pandas as pd
import networkx as nx
from sklearn.feature_extraction.text import CountVectorizer


def build_tdm(comments):
    vec = CountVectorizer()
    X = vec.fit_transform(comments)

    tdm = pd.DataFrame(
        X.toarray().transpose(),
        index=vec.get_feature_names_out()
    )
    tdm.columns = comments.index

    return tdm


def compute_correlation_matrix(tdm):
    return tdm.corr()


def build_edge_dataframe(matcor, threshold=0.6):
    rows = []

    for i in matcor.index:
        for j in matcor.index:
            if i < j:

                w = matcor.loc[i, j]

                if w > threshold:
                    rows.append({
                        "inicio": i,
                        "fin": j,
                        "peso": w
                    })

    cordf = pd.DataFrame(rows)

    return cordf


def build_similarity_graph(cordf):

    G = nx.from_pandas_edgelist(
        cordf,
        source="inicio",
        target="fin",
        edge_attr="peso"
    )

    return G


def get_top_nodes(cdict, num=10):

    return dict(
        sorted(cdict.items(), key=lambda x: x[1], reverse=True)[:num]
    )