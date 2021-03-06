import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

column1 = dbc.Col(
    [
        dcc.Markdown(
            """

            ## Explain

            These predictions were created using data from home sales taken in King County, WA in 2015.

            Originally an XGBoost Regressor model was trained on the entire 21 feature dataset.  Due to time constraints and not wanting to overload the end user with options, I trimmed down the dataset to the 7 features that a prospective homebuyer would be most interested in.

            Unfortunately, this approach severely affected my model's ability to predict prices better.  Trying to find that middle ground between having a really accurate model and not overwhelming the user with a ton of options is fairly problematic.


            to illustrate this discrepancy, I will be doing a side by side comparison of the original model on the full data set, and the smaller more user friendly data set.

            #### First are the feature importances:




            """),
        html.Img(src='/assets/feature_importances_full1.png', style={'width':'45%'}),

            html.Img(src='/assets/feature_importances_trim1.png', style={'width':'45%'}, className='pl-1'),
            dcc.Markdown(
                    """
                    Feature importances on the full data set in red.   Importances on the simplified set in blue

                """,style={'textAlign': 'center'}),
            dcc.Markdown(
                """


            As you can see, a couple of the higher ranked features were dropped, which affected the importance level of the neighboring features.

            Even though 'Grade' was clearly the most important feature in the data set, I was tempted to drop it as well because it wasn't really well defined.  An arbitrary scale from 1-5 without any specific grading criteria, didn't seem like a feature that would be interesting or even important to someone looking to use this tool. Ultimately I let it stay, because of the extreme error removing it caused my model.

            #### Next we have the permutation importances:



                """, className='mt-5'),
            html.Img(src='/assets/permuter_full.png', style={'width':'30%'}, className='mt-3'),
            html.Img(src='/assets/permuter_trim.png', style={'width':'45%'}, className='ml-4'),
            dcc.Markdown(
                    """
                    Permutation importnce of full set on the left, simplified set on the right.

                """,style={'textAlign': 'center'}),
            dcc.Markdown(
                """


            In the first model there are 3 important features (Lat,Long,Zipcode) that I am hoping to implement in the future with a choropleth map of the county.
            Clearly the inclusion of those three features will go a long way to improving upon the models predictive capabilites.

            Another interesting observation was at the lack of importance of the 'bedrooms' feature on both of the models.

            #### How much was accuracy really affected?
            ##### Root Mean Squared Log Error on the full set:


                """, className='mt-5''mb-4'),
            html.Img(src='/assets/RMSLE_full.png', style={'width':'30%'}, className='mb-5'),

            dcc.Markdown(
                """
            ##### Root Mean Squared Log Error on the smaller set:


                """),

            html.Img(src='/assets/RMSLE_trim.png', style={'width':'30%'}),
            dcc.Markdown(
                """
            #### And the accuracy scores (closer to 1.0 is better)
            #### Complete dataframe:


                """, className='mt-5'),
            html.Img(src='/assets/variance_score_full.png', style={'width':'55%'}),
            dcc.Markdown(
                """
            #### Smaller dataframe:


                """, className='mt-5'),
            html.Img(src='/assets/variance_score_trim.png', style={'width':'20%'}),
            dcc.Markdown(
                """
            I think it is important to point out these pronounced discrepancies, to illustrate the difficulties that can be encountered when attempting to deliver a smaller more digestible representation of data to less-technical minded people. Trying to find that balance between overly technical and overly simplistic could almost be the more challenging aspect for us in the workforce.

            In the future I would like to implement a web scraper so that I would be able to update this app with more current information.  As well as figuring out a way to incorporate the geo location elements in the original data set to make an interactive map.


            """, className='mt-5'),





    ],
    md=12,

)


column2 = dbc.Col(
    [

    ]
)

layout = dbc.Row([column1])
