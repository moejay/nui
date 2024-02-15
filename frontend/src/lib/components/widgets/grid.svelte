<script lang="ts">
	import type { GridWidget } from "../../../client";
    import Text from "./text.svelte";

    export let widget: GridWidget;

</script>

<div class="grid grid-cols-{widget.columns} grid-rows-{widget.rows} gap-4">
    {#each widget.widgets as item}
        <div class="bg-slate-400 p-4">
            {#if item.type === "text"}
                <Text widget={item} />
            {:else if item.type === "grid"}
                <svelte:self widget={item} />
            {/if}
        </div>
    {/each}
</div>