/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { StateTree } from '../models/StateTree';
import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';
export class DefaultService {
    /**
     * Read Root
     * @returns StateTree Successful Response
     * @throws ApiError
     */
    public static readRootGet(): CancelablePromise<StateTree> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/',
        });
    }
}
