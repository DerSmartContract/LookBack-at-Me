describe('Reflexions-App', () => {
  beforeEach(() => {
    cy.visit('http://localhost:3000');
  });

  it('Tägliche Reflexionsfrage wird geladen', () => {
    cy.get('[data-testid="daily-question"]').should('not.be.empty');
  });
});