import pandera.pandas as pa

AGE_VALIDATOR = pa.DataFrameSchema({
    "PatientAge": pa.Column(
        int,
        [
            pa.Hypothesis.two_sample_ttest(
                sample1="M",
                sample2="F",
                groupby="PatientSex",
                relationship="equal",
                # relationship="greater_than",
                alpha=0.01,
                equal_var=True,
            ),
        ],
    ),
    "PatientSex": pa.Column(str),
})
