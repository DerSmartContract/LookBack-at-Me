import { test, expect } from '@playwright/test';

test('Tägliche Reflexionsfrage wird geladen', async ({ page }) => {
  await page.goto('http://localhost:3000');
  const question = await page.locator('[data-testid="daily-question"]');
  await expect(question).not.toBeEmpty();
});