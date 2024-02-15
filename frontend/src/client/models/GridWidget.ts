/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { TextWidget } from './TextWidget';
export type GridWidget = {
    /**
     * The unique identifier of the widget within the state tree
     */
    id: number;
    description?: string;
    /**
     * The type of widget, used by the UI to determine how to render the widget
     */
    type?: any;
    /**
     * The number of columns in the grid
     */
    columns: number;
    /**
     * The number of rows in the grid
     */
    rows: number;
    /**
     * The widgets that are children of this grid
     */
    widgets: Array<(GridWidget | TextWidget)>;
};

