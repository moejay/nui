<script lang="ts">
    import { sendMessage, messageHistory } from '$lib/store';
    let message = '';
</script>

<div class="bg-slate-400">
    <input type="text" id="message" bind:value={message} />
    <button on:click={() => sendMessage(message)}>Send</button>
    <div>
        {#each $messageHistory as historyMessage}
            <p>{historyMessage}</p>
        {/each}
    </div>
</div>