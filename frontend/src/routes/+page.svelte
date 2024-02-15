<script lang="ts">
    import { onMount } from 'svelte';
    import { stateTree, connect } from '$lib/store';
	import Chat from '$lib/components/chat.svelte';
	import Grid from '$lib/components/widgets/grid.svelte';

    onMount(() => {
        connect();
    });

    $: stringified = JSON.stringify($stateTree);
</script>

<div>

    <Grid widget={$stateTree.root} />

    <div class="absolute right-2 bottom-2 ">
        <Chat />

    </div>

</div>