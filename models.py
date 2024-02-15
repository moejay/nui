
from typing import Literal, Union
from pydantic import BaseModel, Field

class BaseWidget(BaseModel):
    id: int = Field(description="The unique identifier of the widget within the state tree")
    description: str = Field(description="The description of the widget, used to tell the LLM what the widget does, and how it should be used.")


class GridWidget(BaseWidget):
    type: Literal["grid"] = Field("grid", description="The type of widget, used by the UI to determine how to render the widget")
    description: str = "This GridWidget is used to layout other widgets in a grid."
    columns: int = Field(description="The number of columns in the grid")
    rows: int = Field(description="The number of rows in the grid")
    widgets: list['ALL_WIDGETS'] = Field(description="The widgets that are children of this grid")

class TextWidget(BaseWidget):
    type: Literal["text"] = Field("text", description="The type of widget, used by the UI to determine how to render the widget")
    description: str = "This TextWidget is used to display text."
    text: str = Field(description="The text to display")


ALL_WIDGETS =Union[GridWidget, TextWidget]

GridWidget.update_forward_refs()
class StateTree(BaseModel):
    root:ALL_WIDGETS = Field(description="The root widget of the state tree", discriminator="type")

